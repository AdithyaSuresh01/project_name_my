"""Top-level package for the NumSummarySim project.

This package provides educational utilities for computing numerical summaries
and running simple simulation experiments in pure Python and with NumPy.

Typical usage examples (when installed as a package)::

    from numsummarysim.pure_python_stats import mean, variance
    from numsummarysim.numpy_stats import np_mean
    from numsummarysim.simulation import run_statistic_simulation

When working directly from the source tree, imports may look like::

    from src.pure_python_stats import mean

The code here is intentionally lightweight and didactic rather than
feature-complete.
"""

__all__ = [
    "__version__",
]

__version__ = "0.1.0"
