# Setup and Usage Guide

This document explains how to set up a working environment for the
NumSummarySim project and run the included examples.

## 1. Prerequisites

- Python 3.9 or newer
- Git (optional but recommended)
- Ability to create virtual environments (via `venv`, `conda`, etc.)

## 2. Clone or Download the Project

If you are using Git:

```bash
git clone <your-repository-url> NumSummarySim
cd NumSummarySim
```

Alternatively, download and unpack the project as a ZIP archive and
change into the extracted directory.

## 3. Create and Activate a Virtual Environment

Using the standard library `venv` module:

```bash
python -m venv .venv

# On Unix/macOS
source .venv/bin/activate

# On Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Once activated, your shell prompt should indicate that the virtual
environment is active.

## 4. Install Dependencies

From the project root, run:

```bash
pip install -r requirements.txt
```

This installs core scientific Python packages (NumPy, pandas,
matplotlib, seaborn) and Jupyter Notebook/Lab.

## 5. Running Basic Examples

You can experiment with the functions directly in a Python shell or a
script.

### 5.1 Pure Python stats

```python
from src.pure_python_stats import mean, variance, summary

values = [1, 2, 3, 4, 5]
print("Mean:", mean(values))
print("Variance (sample):", variance(values, ddof=1))
print("Summary:", summary(values))
```

### 5.2 NumPy stats

```python
from src.numpy_stats import np_mean, np_summary

values = [1, 2, 3, 4, 5]
print("NumPy mean:", np_mean(values))
print("NumPy summary:", np_summary(values))
```

### 5.3 Simple simulation

```python
import random
from src.pure_python_stats import mean
from src.simulation import run_statistic_simulation

random.seed(123)

# Sample generator: draws from a Normal(0, 1) distribution
sample_generator = lambda n: [random.gauss(0, 1) for _ in range(n)]

result = run_statistic_simulation(
    sample_generator=sample_generator,
    statistic=mean,
    sample_size=30,
    n_simulations=2000,
)

print("Simulated statistic:", result.statistic_name)
print("Number of simulations:", result.n_simulations)
print("Summary of simulated values:")
for k, v in result.summary.items():
    print(f"  {k}: {v}")
```

## 6. Using the Example Notebook

1. Ensure your virtual environment is active and dependencies installed.
2. From the project root, start Jupyter:

   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. In the Jupyter interface, navigate to `notebooks/` and open
   `numerical_summary_simulation.ipynb`.
4. Run the cells sequentially. The notebook will:
   - Show how to import from `src/`
   - Demonstrate both pure Python and NumPy-based summaries
   - Run simulations and visualize results

## 7. Extending the Project

Ideas for extending or customizing NumSummarySim:

- Add new statistics (e.g., skewness, kurtosis) to `pure_python_stats.py`
  and `numpy_stats.py`.
- Add new sample generators for different distributions (Uniform,
  Exponential, etc.) in scripts or notebooks.
- Implement bootstrap resampling utilities using the existing
  `run_statistic_simulation` framework.
- Enhance the plotting helpers to support additional plot types.

## 8. Troubleshooting

- **ImportError: cannot import name ...**  
  Make sure you are running Python from the project root so that
  ``src/`` is on your import path, or explicitly add it to `PYTHONPATH`.

- **ModuleNotFoundError: No module named 'numpy'**  
  Check that your virtual environment is active and that
  `pip install -r requirements.txt` has completed successfully.

- **Plots not showing in Jupyter**  
  Ensure that you are running the notebook cells in order, and that
  `matplotlib` is installed (it is listed in `requirements.txt`).

If issues persist, try creating a fresh virtual environment and
reinstalling dependencies.
