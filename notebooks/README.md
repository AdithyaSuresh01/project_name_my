# Notebooks

This directory contains Jupyter notebooks that demonstrate how to use the **NumSummarySim** project.

## Contents

- `numerical_summary_simulation.ipynb`  
  An end-to-end, runnable example that:
  - Imports the numerical summary utilities from `src/`
  - Shows pure Python vs NumPy implementations of basic statistics
  - Runs simple simulation experiments to visualize sampling distributions

## Usage

1. Make sure you have installed the project dependencies from the repository root:

   ```bash
   pip install -r requirements.txt
   ```

2. Start Jupyter from the project root (recommended):

   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. Open `notebooks/numerical_summary_simulation.ipynb` and run the cells.

If you run the notebook server from another directory, the first code cell in the notebook attempts to locate and add the `src/` directory to `sys.path` so that imports continue to work.
