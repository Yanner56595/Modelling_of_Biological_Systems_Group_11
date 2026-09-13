# Assignment: Metabolic Modeling (Week 2)

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 11

---

## 1. Repository overview

- `analysis_week2.ipynb` — main analysis notebook containing all required sections
- `KEN3170_Assignment_2026_e_coli_core_expression.csv` — maximal reaction activity data
- `README.md` — this file
- `requirements.txt` — Python dependencies (numpy, matplotlib, pandas, cobra, escher)

**How to run**:
1. Install dependencies: `pip install -r requirements.txt`
2. Open `analysis_week2.ipynb` and run all cells from top to bottom.

---

## 2. Part 1 — Reaction activity visualization

- 1a. Maximal reaction activities in linear pathways
- 1b. Grey arrow values and their meaning

---

## 3. Part 2 — Enzyme activity-constrained metabolic model

Used maximal reaction activity values from e_coli_core_expression.csv in order to contrain the flux bounds of every reaction in the E.coli model. Witht he following rules:
    -Reactions with expression data: If reversible, constrained to -1000 and 1000; If irreversible, contrained to 0 and 1000
    -Reaction with no expression data: Left untouched
    -EX_glc__D_e (glucose exchange): Constrained to -1000 and 1000
    -ATPM: left untouched

Resulting lower and upper bounds for every reaction were printed as a table

---

## 4. Part 3 — Biomass production optimization

- 3a. Maximal biomass production under expression-based constraints
- 3b. Glucose uptake bound of 5 mmol/gDW/h and its interpretation
- 3c. Biomass production rate with the additional glucose uptake constraints, comparison of rates and explanation

---

## 5. Part 4 — Glucose uptake and growth rate analysis

- 4a. Plot of maximal biomass production vs. glucose uptake bound (1–15 mmol/gDW/h, increments of 0.1)
- 4b. Explanation of growth rate limitations with increasing glucose uptake bounds
- 4c. Search for exchange reaction activated in the second curve segment by comparing activated reactions in segment 1 and 2

---

## 6. Conclusions
