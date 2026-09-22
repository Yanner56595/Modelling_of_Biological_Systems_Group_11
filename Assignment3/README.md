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


## 2. Part 2 — Answering questions

### Which mutation is most dangerous and why? Provide quantitative evidence.
Based on the attractor analysis' own metric, all three mutations are tied to the maximun risk, that is: A, B, and C, all have 100% of the 256 possible cancer-like states (growth = 1, Death = 0).

In order to break the tie, the trajectories themselves were inspected, rather than just the end points, resulting in mutation A (p53 KO) being the most dangerous of the four since "p53" and "Death" stay at 0 for the entire trajectory, which results in total abolition of the protective signal.

### Explain the role of feedback loops (e.g., MYC → MDM2 → p53)
In the normal situation there is a clear negative feedback loop between MYC, MDM2 and p53. MYC activates MDM2, then MDM2 inhibits p53 and p53 inhibits MYC directly and inhibits MYC through p21. In all 3 scenarios, this feedback loop is disrupted. So in the situations without mutations, the cell can activate apoptosis when the DNA is damaged, but in the mutated scenarios the cell cannot activate apoptosis and causes cancer cell formation.

### What are the limitations of this Boolean network model? Discuss 3 specific limitations.
1. Discreet: Boolean networks models won't allow to model continuous states, therefore there is no representation of expression levels or partial gene functions. In actual scenarios, there can be differing levels of protein expression and transcription levels that can be different than the binary situation assumed by Boolean networks.

2. Deterministic: A starting point always leads to the same outcome, no noise or randomization is included in the system. This is not realistic for many interaction between genes where data is obtained experimentaly (based on propabilities) and noise is also included, along with random actifacts.

3. Oversimplification: P53 pathway contains other complex and interacting components that exists as a safeguard from situations like mutation B and C, which is why they reach 100% cancer-like states as cleanly as a direct p53 knouckout. 
There are also missing pathways that influence the effect mutation A, B and C would have in an actual situation. By leaving these outside of the model, we might make conclusions that turn out to be false in experimental settings.