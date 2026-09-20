# Assignment: Network Biology (Week 3)

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 11

---

## 1. Repository overview

- `analysis3.ipynb` — main analysis notebook containing all required sections
- `README.md` — this file
- `requirements.txt` — Python dependencies (numpy, matplotlib, pandas, networkx, seaborn)

**How to run**:
1. Install dependencies: `pip install -r requirements.txt`
2. Open `analysis_week2.ipynb` and run all cells from top to bottom.

---

## 2. Part 1 — Mutated Networks


## 3. Part 2 — Scenario Analysis


## 4. Part 3 — Attractor Analysis


## 5. Part 4 — Answering questions

### Which mutation is most dangerous and why? Provide quantitative evidence.
Based on the attractor analysis' own metric, all three mutations are tied to the maximun risk, that is: A, B, and C, all have 100% of the 256 possible cancer-like states (growth = 1, Death = 0).

In order to break the tie, the trajectories themselves were inspect, rather than just the end points, resulting in mutation A (p53 KO) being the most dangerous of the four since "p53" and "Death" stay at 0 for the entire trajectory, which results in total abolition of the protective signal.

### Explain the role of feedback loops (e.g., MYC → MDM2 → p53)
Feedback loops allow the network to be mutually antagonistic, meaning that each side actively represses the other's ability to win. This is critical in biology since, in order to reach a discrete state (Death/growth), only one outcome can be true at the same time.

### What are the limitations of this Boolean network model? Discuss 3 specific limitations.
1. Discreet: Boolean networks models won't allow to model continuous states, therefore there is no representation of expression levels or partial gene functions.

2. Deterministic: A starting point always leads to the same outcome, no noise or randomization is included in the system. This is not realistic for many interaction between genes where data is obtained experimentaly (based on propabilities) and noise is also included, along with random actifacts.

3. Oversimplification: P53 pathway contains other complex and interacting components that exists as a safeguard from sutuations like mutation B and C, which is why they reach 100% cancer-like states as cleanly as a direct p53 knouckout