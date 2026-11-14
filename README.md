# FHtorch Oxy-Fuel Cutting Tip Chart

Free, open data and a simple size picker for oxy-fuel cutting tips:
**Victor-type 1-101 and GPN, Harris-type 6290 and 6290NXM, British-style ANM, ANME and PNME, and type A LPG nozzles.**

Made by [FHtorch](https://fhtorch.com/?utm_source=github&utm_medium=readme&utm_campaign=cutting-tip-chart), an oxy-fuel cutting and welding torch factory in Ningbo, China.

**Use it online:** https://fhtorch.github.io/cutting-tip-chart/

## What it does

- Choose the fuel gas, the steel thickness (mm or inches) and the torch style. The picker lists every tip size whose cutting range covers that thickness, with the orifice size and the oxygen and fuel gas pressures from the chart (MPa and psi).
- The full chart is below, and the same data is in [`data/`](data/) as JSON and CSV, for your own catalog, website or quoting sheet.
- No sign-up, no tracking, no build step: `index.html` works from GitHub Pages or straight from a downloaded copy.

## The data

- Every record comes from a specification table on an FHtorch product page, and keeps its `source_url`.
- Values are FHtorch catalog values for FHtorch tips. Cutting thickness is for steel, as stated on those pages. Some families list sizes and cutting ranges only, without pressures.
- Rebuild the files from the live pages with `python scripts/build_data.py` (Python 3, no packages needed).

| Field | Meaning |
|---|---|
| `family`, `model` | Tip family (e.g. `1-101`) and FHtorch model number |
| `torch_style` | Victor-type, Harris-type, British-style or Type A (two-piece) |
| `fuel_gases` | Fuel gases the family is made for |
| `size` | Tip size as marked (e.g. `000`, `3`, `1/16`) |
| `orifice_mm` | Cutting oxygen orifice, mm |
| `cut_min_mm`, `cut_max_mm` | Cutting thickness range, mm |
| `oxygen_mpa_min`, `oxygen_mpa_max` | Oxygen pressure from the chart, MPa |
| `fuel_mpa_min`, `fuel_mpa_max` | Fuel gas pressure from the chart, MPa |
| `fits`, `source_url` | What the tips fit, and the page the row comes from |

## Chart

<!-- CHART:START -->

### 1-101 (Victor-type, acetylene)

Fits Victor-type cutting torches and cutting attachments. Source: [fhtorch.com/product/1-101-cutting-tips/](https://fhtorch.com/product/1-101-cutting-tips/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) | Oxygen (MPa) | Fuel gas (MPa) |
|---|---|---|---|---|
| 000 | 0.7 | 1–3 | 0.15–0.2 | 0.035 |
| 00 | 0.8 | 3–6 | 0.15–0.2 | 0.035 |
| 0 | 1 | 6–10 | 0.2–0.25 | 0.035 |
| 1 | 1.2 | 10–20 | 0.2–0.25 | 0.035 |
| 2 | 1.5 | 20–40 | 0.25–0.32 | 0.045 |
| 3 | 1.8 | 40–60 | 0.25–0.35 | 0.06 |
| 4 | 2.1 | 60–80 | 0.32–0.4 | 0.07 |
| 5 | 2.5 | 80–125 | 0.32–0.4 | 0.085 |
| 6 | 3 | 125–200 | 0.32–0.56 | 0.095 |
| 7 | 3.5 | 200–250 | 0.32–0.56 | 0.1 |
| 8 | 4 | 250–300 | 0.4–0.6 | 0.1 |

### GPN (Victor-type, propane, natural gas)

Fits Victor-type cutting torches. Source: [fhtorch.com/product/gpn-cutting-tips/](https://fhtorch.com/product/gpn-cutting-tips/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) | Oxygen (MPa) | Fuel gas (MPa) |
|---|---|---|---|---|
| 000 | 0.7 | 1–3 | 0.14–0.25 | 0.021–0.035 |
| 00 | 0.8 | 3–6 | 0.14–0.25 | 0.021–0.035 |
| 0 | 1 | 6–10 | 0.21–0.28 | 0.021–0.035 |
| 1 | 1.2 | 10–20 | 0.21–0.28 | 0.028–0.042 |
| 2 | 1.5 | 20–40 | 0.28–0.35 | 0.035–0.063 |
| 3 | 1.8 | 40–60 | 0.31–0.34 | 0.042–0.069 |
| 4 | 2.1 | 60–80 | 0.31–0.34 | 0.056–0.083 |
| 5 | 2.5 | 80–125 | 0.34–0.38 | 0.056–0.083 |
| 6 | 3.1 | 125–200 | 0.38 | 0.069–0.1 |
| 7 | 3.6 | 200–250 | 0.38 | 0.069–0.1 |
| 8 | 4.1 | 250–300 | 0.38 | 0.069–0.1 |

### 6290 (Harris-type, acetylene)

Fits Harris-type equipment, including the FHtorch 72-3 cutting attachment. Source: [fhtorch.com/product/6290-cutting-tips/](https://fhtorch.com/product/6290-cutting-tips/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) |
|---|---|---|
| 000 | 0.8 | 1–5 |
| 00 | 0.7 | 5–10 |
| 0 | 1 | 10–15 |
| 1 | 1.2 | 15–25 |
| 2 | 1.6 | 25–50 |
| 3 | 1.9 | 50–100 |
| 4 | 2.4 | 100–175 |
| 5 | 2.8 | 175–250 |
| 6 | 3.2 | 250–300 |

### 6290NXM (Harris-type, propane)

Fits Harris-type torches and cutting attachments. Source: [fhtorch.com/product/6290nxm-propane-cutting-tips/](https://fhtorch.com/product/6290nxm-propane-cutting-tips/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) | Oxygen (MPa) | Fuel gas (MPa) |
|---|---|---|---|---|
| 000 | 0.8 | 1–5 | 0.2 | 0.034–0.12 |
| 00 | 0.9 | 5–10 | 0.14–0.21 | 0.034–0.12 |
| 0 | 1 | 10–15 | 0.21–0.28 | 0.034–0.12 |
| 1 | 1.2 | 15–25 | 0.24–0.34 | 0.034–0.12 |
| 2 | 1.6 | 25–50 | 0.28–0.38 | 0.034–0.12 |
| 3 | 2 | 50–100 | 0.31–0.41 | 0.034–0.12 |
| 4 | 2.4 | 100–175 | 0.34–0.52 | 0.034–0.12 |
| 5 | 2.8 | 175–250 | 0.45–0.55 | 0.034–0.12 |
| 6 | 3.2 | 250–300 | 0.5–0.62 | 0.034–0.12 |

### ANME (British-style, acetylene)

Fits British-style hand cutting torches such as the NM-250 and G02-200. Source: [fhtorch.com/product/anm-anme-acetylene-cutting-nozzles/](https://fhtorch.com/product/anm-anme-acetylene-cutting-nozzles/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) |
|---|---|---|
| 1/32 | 0.8 | 3–10 |
| 3/64 | 1.2 | 10–25 |
| 1/16 | 1.6 | 25–40 |
| 5/64 | 2 | 40–60 |
| 3/32 | 2.4 | 60–100 |
| 7/64 | 2.8 | 100–200 |
| 1/8 | 3.2 | 200–300 |

### ANM (British-style, acetylene)

Fits British-style hand cutting torches such as the NM-250 and G02-200. Source: [fhtorch.com/product/anm-anme-acetylene-cutting-nozzles/](https://fhtorch.com/product/anm-anme-acetylene-cutting-nozzles/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) | Oxygen (MPa) | Fuel gas (MPa) |
|---|---|---|---|---|
| 1/32 | 0.9 | 3–10 | 0.2–0.35 | 0.014 |
| 3/64 | 1.2 | 10–25 | 0.3–0.5 | 0.02 |
| 1/16 | 1.6 | 25–40 | 0.4–0.55 | 0.025 |
| 5/64 | 2 | 40–60 | 0.45–0.6 | 0.035 |
| 3/32 | 2.4 | 60–100 | 0.5–0.65 | 0.035 |
| 7/64 | 2.8 | 100–200 | 0.45–0.8 | 0.04 |
| 1/8 | 3.3 | 200–300 | 0.75–0.85 | 0.045 |

### PNME9 (British-style, propane, LPG)

Fits British-style hand cutting torches. Source: [fhtorch.com/product/pnme-propane-cutting-nozzles/](https://fhtorch.com/product/pnme-propane-cutting-nozzles/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) | Oxygen (MPa) | Fuel gas (MPa) |
|---|---|---|---|---|
| 1/32 | 0.8 | 3–10 | 0.3–0.5 | 0.02 |
| 3/64 | 1.2 | 10–25 | 0.3–0.5 | 0.025 |
| 1/16 | 1.6 | 25–40 | 0.4–0.55 | 0.03 |
| 5/64 | 2 | 40–60 | 0.45–0.6 | 0.035 |
| 3/32 | 2.4 | 60–100 | 0.5–0.65 | 0.04 |
| 7/64 | 2.8 | 100–200 | 0.45–0.8 | 0.045 |
| 1/8 | 3.2 | 200–300 | 0.75–0.85 | 0.05 |

### PNME18 (British-style, propane, LPG)

Fits British-style hand cutting torches. Source: [fhtorch.com/product/pnme-propane-cutting-nozzles/](https://fhtorch.com/product/pnme-propane-cutting-nozzles/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) |
|---|---|---|
| 1/64 | 0.6 | 1–3 |
| 1/32 | 0.8 | 3–10 |
| 3/64 | 1.2 | 10–25 |
| 1/16 | 1.6 | 25–75 |
| 5/64 | 2 | 75–125 |
| 3/32 | 2.4 | 125–175 |
| 7/64 | 2.8 | 175–225 |
| 1/8 | 3.2 | 225–300 |

### Type A (Type A (two-piece), LPG)

Fits two-piece type A nozzles (brass body, copper tip). Source: [fhtorch.com/product/type-a-lpg-cutting-nozzles/](https://fhtorch.com/product/type-a-lpg-cutting-nozzles/?utm_source=github&utm_medium=readme)

| Size | Orifice (mm) | Cutting thickness (mm) |
|---|---|---|
| 1 | 1 | 1–15 |
| 2 | 1.3 | 15–50 |
| 3 | 1.6 | 50–100 |

<!-- CHART:END -->

## Safety

These are chart values for FHtorch tips. Always follow the instructions of your torch and regulator manufacturer, and your local safety rules.

## About FHtorch

FHtorch supplies distributors and welding supply stores with cutting torches, welding torches, cutting and welding tips, flashback arrestors and torch kits. Our torches are made at our family-owned factory in Ningbo, China, registered in 2019. MOQ 100–300 units per model; custom logo marking (OEM) available.

- Website: https://fhtorch.com/?utm_source=github&utm_medium=readme&utm_campaign=cutting-tip-chart
- Cutting tips: https://fhtorch.com/product-category/cutting-tips/?utm_source=github&utm_medium=readme&utm_campaign=cutting-tip-chart
- Request a quote: https://fhtorch.com/contact/?utm_source=github&utm_medium=readme&utm_campaign=cutting-tip-chart

## License

- Code (`index.html`, `scripts/`): [MIT](LICENSE).
- Data (`data/`): [CC BY 4.0](LICENSE-DATA). Please credit "FHtorch (fhtorch.com)".

## Trademarks

Victor® and Harris® are trademarks of their respective owners. FHtorch is not affiliated with them; "Victor-type" and "Harris-type" describe the style and fit of FHtorch products.
