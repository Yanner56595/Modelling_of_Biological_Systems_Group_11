# Assignment: Metabolic Modeling (Week 2)

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 11

---

## 1. Repository overview

- `analysis_week2.ipynb` — main analysis notebook
- `KEN3170_Assignment_2026_e_coli_core_expression.csv` — maximal reaction activity data
- `README.md` — this file

**How to run**: [Add setup and execution instructions]

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

<!-- - 3a. Maximal biomass production under enzyme activity constraints
- 3b. Glucose uptake bound of 5 mmol/gDW/h and its interpretation
- 3c. Biomass production with the additional glucose uptake constraint -->

---

## 5. Part 4 — Glucose uptake and growth rate analysis

<!-- - 4a. Maximal biomass production versus glucose uptake bound (1–15 mmol/gDW/h, increments of 0.1)
- 4b. Growth rate limitations with increasing glucose uptake bounds
- 4c. Exchange reaction activated in the second curve segment -->

---

## 6. Conclusions
