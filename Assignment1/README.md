# Epidemiological Model Assignment — Parameter Exploration

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 11

---

## 1. Repository overview
- `analysis.ipynb` — main notebook containing all required sections (Setup, Part 1–3, Conclusions)
- `requirements.txt` — Python dependencies (numpy, matplotlib, pandas, scipy, seaborn)
- `README.md` — this file

**How to run**:
1. Install dependencies: `pip install -r requirements.txt`
2. Open `analysis.ipynb` and run all cells from top to bottom.

---

## 2. Part 1 — Parameter analysis function
**Function**: `analyze_recovery_rates(beta, mu, N, I0, simulation_days)`
**Approach**:
We implemented a SIRD (Susceptible, Infectious, Recovered, Dead) model using ordinary differential equations. The function loops through a set of recovery rates ($\gamma \in [0.05, 0.1, 0.15, 0.2, 0.25]$) to evaluate their impact on the epidemic trajectory while keeping other parameters fixed. In contrast to the task description, we used the corrected formula for the basic reproduction number in an SIRD model, calculating it as $R_0 = \beta / (\gamma + \mu)$, since both recovery and mortality remove infectious individuals from calculations.
**Output**:
The function generates `pandas.DataFrame` and epidemic curve plot. The dataframe contains the following metrics for each $\gamma$ value:
- `gamma`: The recovery rate tested.
- `R0`: The calculated basic reproduction number.
- `peak_infected`: The maximum number of concurrently infectious individuals.
- `peak_day`: The simulation day on which the peak occurs.
- `total_deaths`: Cumulative deaths by the end of the simulation.
- `epidemic_duration`: The number of days until the infectious population drops below 1.

---

## 3. Part 2 — Scenario comparison
We evaluated two distinct public health scenarios over a 200-day simulation with a population of 1000:
* **Scenario A (High Transmission)**: $\beta=0.4$, $\mu=0.02$
* **Scenario B (Low Transmission)**: $\beta=0.2$, $\mu=0.005$
### 3.1 Scenario Results:
**High Transmission Scenario:**

|   | gamma |       R0 | peak_infected | peak_day | total_deaths | epidemic_duration |
|--:|------:|---------:|--------------:|---------:|-------------:|------------------:|
| 0 |  0.05 | 5.714286 |    520.582635 |       21 |   284.757361 |               118 |
| 1 |  0.10 | 3.333333 |    340.140583 |       22 |   159.892366 |                86 |
| 2 |  0.15 | 2.352941 |    213.465894 |       24 |   102.610885 |                77 |
| 3 |  0.20 | 1.818182 |    123.893909 |       27 |    67.423926 |                78 |
| 4 |  0.25 | 1.481481 |     63.051893 |       30 |    42.694003 |                84 |

**Low Transmission Scenario:**

|   | gamma |       R0 | peak_infected | peak_day | total_deaths | epidemic_duration |
|--:|------:|---------:|--------------:|---------:|-------------:|------------------:|
| 0 |  0.05 | 3.636364 |    371.356334 |       44 |    88.224137 |               178 |
| 1 |  0.10 | 1.904762 |    139.333450 |       52 |    36.699911 |               154 |
| 2 |  0.15 | 1.290323 |     31.340756 |       67 |    13.640017 |               185 |
| 3 |  0.20 | 0.975610 |      5.000000 |        0 |     1.831032 |               116 |
| 4 |  0.25 | 0.784314 |      5.000000 |        0 |     0.433166 |                28 |
### 3.2 Scenario Analysis
**Result Summary**:
Scenario A is significantly worse than scenario B. Due to the high transmission and mortality rates, $R_0$ remains high and > 1 across almost all tested recovery rates, resulting in earlier and higher peak of infected people and total deaths than in low transmission scenario. The work load for hospitals in such scenario is much higher, which in real life would lead even to more severe consequences.

---

## 4. Part 3 — Policy recommendations
### 4.1 Parameter impact analysis
Increasing the recovery rate ($\gamma$) reliably flattens the epidemic curve and reduces fatalities. Using Scenario A as an example, shifting $\gamma$ from 0.05 to 0.25 yields:
* **87.9% reduction in peak infections** (dropping from ~520.6 to 63.1).
* **85.0% reduction in total deaths** (dropping from ~284.8 to 42.7).
* A delay in peak hospital burden, pushing the peak day from Day 21 to Day 30.

Interestingly, the effect on **epidemic duration is non-monotonic**. While raising $\gamma$ from 0.05 to 0.15 shortens the epidemic from 118 days to 77 days, pushing $\gamma$ even higher to 0.25 extends the duration back out to 84 days. The highest recovery rates create a much safer, flatter curve, but the disease "smolders" at low levels for slightly longer.

### 4.2 Intervention analysis
If a medical intervention increased the recovery rate by 50% in Scenario A (shifting $\gamma$ from a baseline of 0.10 to 0.15), the mathematical model predicts:
* A drop in total deaths from roughly 159.89 to 102.61.
* A **35.8% relative reduction in mortality**.
* Approximately 57 lives saved per 1,000 individuals.
This demonstrates the non-linear dynamics of epidemic modeling: a 50% improvement in recovery rate results in a smaller (35.8%), but still highly significant, reduction in total fatalities.
### 4.3 Real-world application
**Antibiotic treatment for bacterial infections** (such as uncomplicated urinary tract infections) serves as a real-world equivalent to increasing $\gamma$. 
By inhibiting bacterial replication and reducing pathogen load, antibiotics allow patients to clear the infection faster. Based on clinical trials, prescribing antibiotics reduces the median recovery time of an uncomplicated UTI from roughly 9 days (natural resolution) to 7 days. In the context of an SIRD model, this effectively increases the $\gamma$ parameter from $\approx 0.11$ to $\approx 0.14$, limiting the window of transmission and reducing peak epidemic load.

---

## 5. Conclusions
This assignment demonstrated how mathematical modeling is used to evaluate the trajectory of an epidemic under varying biological and public health parameters. By systematically varying the recovery rate ($\gamma$) within an SIRD framework, we quantified the non-linear relationship between recovery time, peak infection loads, and mortality. Furthermore, translating these mathematical shifts into real-world medical interventions—such as the distribution of antibiotics—highlights the critical role computational models play in optimizing public health strategies and evaluating the efficacy of proposed interventions.