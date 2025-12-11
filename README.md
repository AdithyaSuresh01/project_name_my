# NumSummarySim

NumSummarySim is a small educational project demonstrating how to compute basic **numerical summaries** (mean, median, variance, quantiles, correlations, etc.) using both **pure Python** and **NumPy**, and how to run simple **simulation experiments** to explore the behavior of these statistics.

The project is organized to be beginner-friendly while still following modern Python project layout conventions:

- Core functionality lives under `src/`
- Example data lives under `data/`
- Jupyter notebooks live under `notebooks/`
- Longer-form documentation lives under `docs/`

---

## Features

- **Pure Python implementations** of common descriptive statistics:
  - Mean, median, variance, standard deviation
  - Minimum, maximum, range
  - Quantiles and interquartile range (IQR)
  - Covariance and correlation (Pearson)
- **NumPy-based implementations** of the same statistics for performance and validation
- **Simulation utilities** to:
  - Generate repeated samples from simple distributions
  - Compute statistics across simulations
  - Compare empirical distribution of statistics vs theoretical expectations
- **Plotting helpers** to quickly visualize simulation results in notebooks.

---

## Quick Start

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Explore in a Python shell

```bash
python
```

```python
from src.pure_python_stats import mean, variance
from src.numpy_stats import np_mean, np_variance
from src.simulation import run_statistic_simulation

# Basic stats
values = [1, 2, 3, 4, 5]
print("Mean:", mean(values))
print("Variance:", variance(values, ddof=1))

# Simulation: sample means from a normal distribution
import random

random.seed(42)

result = run_statistic_simulation(
    sample_generator=lambda n: [random.gauss(0, 1) for _ in range(n)],
    statistic=mean,
    sample_size=30,
    n_simulations=1_000,
)

print("Number of simulations:", result.n_simulations)
print("Approximate mean of sample means:", result.summary["mean"])  # Mean of the simulated means
```

---

## Using the Notebooks

1. Ensure your virtual environment is activated and dependencies are installed.
2. Start Jupyter:

   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. Open `notebooks/numerical_summary_simulation.ipynb` and run the cells sequentially.

The notebook demonstrates:

- Computing numerical summaries using both pure Python and NumPy
- Running simulations to explore sampling distributions (e.g., of the sample mean)
- Visualizing results with histograms and line plots.

---

## Project Structure

```text
NumSummarySim/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   └── sample_sales_data.csv
├── docs/
│   ├── PROJECT_OVERVIEW.md
│   └── SETUP_AND_USAGE.md
├── notebooks/
│   ├── numerical_summary_simulation.ipynb
│   └── README.md
└── src/
    ├── __init__.py
    ├── pure_python_stats.py
    ├── numpy_stats.py
    ├── simulation.py
    └── utils/
        ├── __init__.py
        └── plotting_helpers.py
```

---

## Minimal Example: Comparing Pure Python vs NumPy

```python
from src.pure_python_stats import mean, variance
from src.numpy_stats import np_mean, np_variance

values = [10, 12, 13, 9, 11, 8, 15]

print("Pure Python mean:", mean(values))
print("NumPy mean:", np_mean(values))
print("Pure Python variance (ddof=1):", variance(values, ddof=1))
print("NumPy variance (ddof=1):", np_variance(values, ddof=1))
```

---

## License

This project is provided for educational and demonstration purposes. Add a specific open-source license file (e.g., MIT) if you intend to publish or share this project widely.
