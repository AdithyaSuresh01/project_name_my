# NumSummarySim – Project Overview

## Purpose

NumSummarySim is an educational mini-project aimed at helping learners
understand **numerical summary statistics** and **simulation-based
reasoning** in introductory statistics and data science.

Rather than focusing on advanced statistical modeling, the project
emphasizes:

- How to compute and interpret basic descriptive statistics
- The relationship between pure Python implementations and
  vectorized NumPy operations
- How repeated simulation can reveal the behavior of estimators
  (e.g., sampling distributions, variability vs. sample size)

## Core Concepts Illustrated

1. **Descriptive statistics**
   - Measures of central tendency: mean, median
   - Measures of spread: range, interquartile range (IQR), variance,
     standard deviation
   - Quantiles and empirical percentiles
2. **Relationships between variables**
   - Covariance
   - Pearson correlation
3. **Sampling and simulation**
   - Generating repeated samples from simple distributions
   - Computing statistics on each sample
   - Inspecting the distribution of those statistics across simulations

## Components

- `src/pure_python_stats.py`  
  Transparent, from-scratch implementations of basic statistics, useful
  for teaching and for verifying understanding of underlying formulas.

- `src/numpy_stats.py`  
  Equivalent implementations using NumPy, illustrating the benefits of
  vectorization and showing how high-level library calls relate to
  simple algorithms.

- `src/simulation.py`  
  A generic simulation runner that repeatedly draws samples from a
  user-provided data-generating function and computes a user-provided
  statistic.

- `src/utils/plotting_helpers.py`  
  Small, opinionated helpers for visualizing simulation results in
  notebooks.

- `notebooks/numerical_summary_simulation.ipynb`  
  An executable walkthrough tying the above components together.

## Intended Audience

- Students in introductory statistics / data science courses
- Instructors seeking minimal, inspectable examples to support lectures
- Practitioners wanting a concise reference implementation of common
  descriptive statistics

## What This Project Is Not

- It is **not** a full-featured statistics library.
- It is **not** optimized for very large datasets or high-performance
  production use.
- It is **not** a replacement for established libraries such as
  NumPy, SciPy, pandas, or statsmodels.

Instead, NumSummarySim is deliberately small and didactic, making it
suitable as a learning tool, code-reading exercise, and a basis for
small classroom assignments.
