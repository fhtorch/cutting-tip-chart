"""Build the cutting tip dataset from FHtorch's public product pages.

Reads the specification tables on each tip page of https://fhtorch.com, then writes:
  data/cutting-tips.json   one record per tip size
  data/cutting-tips.csv    same records, flat
  data/cutting-tips.js     window.FH_TIPS = [...] for index.html (works from file:// too)
  README.md                the chart tables between the CHART markers

Usage: python scripts/build_data.py
No third-party packages needed.
"""
import csv
import html
import json
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (compatible; fhtorch-cutting-tip-chart/1.0; +https://github.com/fhtorch/cutting-tip-chart)"
MPA_TO_PSI = 145.0377

# One entry per tip family. Facts (style, gases, fit) are taken from the same product pages.
FAMILIES = [
    {"family": "1-101", "model": "MH005-001", "style": "Victor-type", "gases": ["acetylene"],
     "fits": "Victor-type cutting torches and cutting attachments",
     "url": "https://fhtorch.com/product/1-101-cutting-tips/", "table": 0},
    {"family": "GPN", "model": "MH005-002", "style": "Victor-type", "gases": ["propane", "natural gas"],
     "fits": "Victor-type cutting torches",
     "url": "https://fhtorch.com/product/gpn-cutting-tips/", "table": 0},
    {"family": "6290", "model": "MH005-003", "style": "Harris-type", "gases": ["acetylene"],
     "fits": "Harris-type equipment, including the FHtorch 72-3 cutting attachment",
     "url": "https://fhtorch.com/product/6290-cutting-tips/", "table": 0},
    {"family": "6290NXM", "model": "MH005-004", "style": "Harris-type", "gases": ["propane"],
     "fits": "Harris-type torches and cutting attachments",
     "url": "https://fhtorch.com/product/6290nxm-propane-cutting-tips/", "table": 0},
    {"family": "ANME", "model": "MH005-005", "style": "British-style", "gases": ["acetylene"],
     "fits": "British-style hand cutting torches such as the NM-250 and G02-200",
     "url": "https://fhtorch.com/product/anm-anme-acetylene-cutting-nozzles/", "table": "ANME"},
    {"family": "ANM", "model": "MH005-008", "style": "British-style", "gases": ["acetylene"],
     "fits": "British-style hand cutting torches such as the NM-250 and G02-200",
     "url": "https://fhtorch.com/product/anm-anme-acetylene-cutting-nozzles/", "table": "ANM nozzles"},
    {"family": "PNME9", "model": "MH005-006", "style": "British-style", "gases": ["propane", "LPG"],
     "fits": "British-style hand cutting torches",
     "url": "https://fhtorch.com/product/pnme-propane-cutting-nozzles/", "table": "PNME9"},
    {"family": "PNME18", "model": "MH005-007", "style": "British-style", "gases": ["propane", "LPG"],
     "fits": "British-style hand cutting torches",
     "url": "https://fhtorch.com/product/pnme-propane-cutting-nozzles/", "table": "PNME18"},
    {"family": "Type A", "model": "MH005-009", "style": "Type A (two-piece)", "gases": ["LPG"],
     "fits": "two-piece type A nozzles (brass body, copper tip)",
     "url": "https://fhtorch.com/product/type-a-lpg-cutting-nozzles/", "table": 0},
]


class Tables(HTMLParser):
    """Collects tables inside the product description, each with the nearest heading before it."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables, self.heading, self._h, self._cell, self._row, self._tab = [], None, None, None, None, None

    def handle_starttag(self, tag, attrs):
        if tag in ("h2", "h3", "h4"):
            self._h = ""
        elif tag == "table":
            self._tab = {"heading": self.heading, "head": [], "rows": []}
        elif tag == "tr" and self._tab is not None:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = ""

    def handle_endtag(self, tag):
        if tag in ("h2", "h3", "h4") and self._h is not None:
            self.heading, self._h = self._h.strip(), None
        elif tag in ("td", "th") and self._cell is not None:
            self._row.append(re.sub(r"\s+", " ", self._cell).strip())
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._row:
                if not self._tab["head"]:
                    self._tab["head"] = self._row
                else:
                    self._tab["rows"].append(self._row)
            self._row = None
        elif tag == "table" and self._tab is not None:
            self.tables.append(self._tab)
            self._tab = None

    def handle_data(self, data):
        if self._h is not None:
            self._h += data
        if self._cell is not None:
            self._cell += data


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def num_range(s):
    """'1–3' -> (1.0, 3.0); '0.38' -> (0.38, 0.38); '' -> (None, None)."""
    s = html.unescape(s).replace(",", ".").replace("–", "-").replace("—", "-").strip()
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", s)]
    if not nums:
        return None, None
    return nums[0], nums[-1]


def col(head, *names):
    for i, h in enumerate(head):
        hl = h.lower()
        if any(n in hl for n in names):
            return i
    return None


def main():
    pages, records = {}, []
    for fam in FAMILIES:
        if fam["url"] not in pages:
            page = fetch(fam["url"])
            m = re.search(r'id="tab-description"(.*?)</div>\s*</div>', page, re.S) or re.search(r'(<h2>Specifications</h2>.*)', page, re.S)
            parser = Tables()
            parser.feed(m.group(1) if m else page)
            pages[fam["url"]] = parser.tables
        tables = pages[fam["url"]]
        if isinstance(fam["table"], int):
            tab = tables[fam["table"]]
        else:
            tab = next(t for t in tables if t["heading"] and fam["table"] in t["heading"])
        head = tab["head"]
        i_size, i_orif, i_cut = col(head, "size"), col(head, "orifice"), col(head, "cutting thickness")
        i_o2 = col(head, "oxygen pressure")
        i_fuel = col(head, "acetylene pressure", "propane pressure", "fuel gas pressure")
        for row in tab["rows"]:
            cut_min, cut_max = num_range(row[i_cut])
            o2_min, o2_max = num_range(row[i_o2]) if i_o2 is not None else (None, None)
            f_min, f_max = num_range(row[i_fuel]) if i_fuel is not None else (None, None)
            records.append({
                "family": fam["family"], "model": fam["model"], "torch_style": fam["style"],
                "fuel_gases": fam["gases"], "fits": fam["fits"], "size": row[i_size],
                "orifice_mm": num_range(row[i_orif])[0],
                "cut_min_mm": cut_min, "cut_max_mm": cut_max,
                "oxygen_mpa_min": o2_min, "oxygen_mpa_max": o2_max,
                "fuel_mpa_min": f_min, "fuel_mpa_max": f_max,
                "source_url": fam["url"],
            })
        print(f"{fam['family']:8s} {len(tab['rows']):2d} rows  {fam['url']}")

    data_dir = os.path.join(ROOT, "data")
    os.makedirs(data_dir, exist_ok=True)
    meta = {"name": "FHtorch oxy-fuel cutting tip chart", "source": "https://fhtorch.com",
            "license": "CC BY 4.0 (attribution: FHtorch, https://fhtorch.com)",
            "units": {"orifice": "mm", "cutting thickness": "mm (mild steel)", "pressure": "MPa"},
            "records": records}
    with open(os.path.join(data_dir, "cutting-tips.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    with open(os.path.join(data_dir, "cutting-tips.js"), "w", encoding="utf-8") as f:
        f.write("// Generated by scripts/build_data.py from https://fhtorch.com product pages. CC BY 4.0, FHtorch.\n")
        f.write("window.FH_TIPS = " + json.dumps(records, ensure_ascii=False) + ";\n")
    fields = ["family", "model", "torch_style", "fuel_gases", "size", "orifice_mm", "cut_min_mm", "cut_max_mm",
              "oxygen_mpa_min", "oxygen_mpa_max", "fuel_mpa_min", "fuel_mpa_max", "fits", "source_url"]
    with open(os.path.join(data_dir, "cutting-tips.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in records:
            w.writerow({**{k: r[k] for k in fields}, "fuel_gases": ";".join(r["fuel_gases"])})

    # README chart section
    def fmt(a, b):
        if a is None:
            return "–"
        return f"{a:g}" if a == b else f"{a:g}–{b:g}"

    lines = []
    for fam in FAMILIES:
        rows = [r for r in records if r["family"] == fam["family"]]
        lines.append(f"### {fam['family']} ({fam['style']}, {', '.join(fam['gases'])})\n")
        lines.append(f"Fits {fam['fits']}. Source: [{fam['url'].replace('https://', '')}]({fam['url']}?utm_source=github&utm_medium=readme)\n")
        has_p = any(r["oxygen_mpa_min"] is not None for r in rows)
        if has_p:
            lines.append("| Size | Orifice (mm) | Cutting thickness (mm) | Oxygen (MPa) | Fuel gas (MPa) |")
            lines.append("|---|---|---|---|---|")
        else:
            lines.append("| Size | Orifice (mm) | Cutting thickness (mm) |")
            lines.append("|---|---|---|")
        for r in rows:
            cells = [r["size"], fmt(r["orifice_mm"], r["orifice_mm"]), fmt(r["cut_min_mm"], r["cut_max_mm"])]
            if has_p:
                cells += [fmt(r["oxygen_mpa_min"], r["oxygen_mpa_max"]), fmt(r["fuel_mpa_min"], r["fuel_mpa_max"])]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")
    readme = os.path.join(ROOT, "README.md")
    if os.path.exists(readme):
        txt = open(readme, encoding="utf-8").read()
        new = re.sub(r"(<!-- CHART:START -->).*?(<!-- CHART:END -->)",
                     lambda m: m.group(1) + "\n\n" + "\n".join(lines) + "\n" + m.group(2), txt, flags=re.S)
        open(readme, "w", encoding="utf-8").write(new)
    print(f"{len(records)} records written")


if __name__ == "__main__":
    sys.exit(main())
