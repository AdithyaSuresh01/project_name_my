"""NumPy-based implementations of basic numerical summary statistics.

This module mirrors the functionality of :mod:`pure_python_stats` but
leverages NumPy for concise and efficient computation. It is also useful
for validating the pure-Python versions.
"""

from __future__ import annotations

from typing import Iterable, Dict

import numpy as np


def _to_ndarray(values: Iterable[float]) -> np.ndarray:
    """Convert *values* to a one-dimensional float NumPy array.

    Raises
    ------
    ValueError
        If the sequence is empty.
    """

    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        raise ValueError("Cannot compute statistic on an empty sequence.")
    return arr


def np_mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(arr.mean())


def np_median(values: Iterable[float]) -> float:
    """Return the median of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(np.median(arr))


def np_min(values: Iterable[float]) -> float:
    """Return the minimum of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(arr.min())


def np_max(values: Iterable[float]) -> float:
    """Return the maximum of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(arr.max())


def np_range(values: Iterable[float]) -> float:
    """Return the range (max - min) of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(arr.max() - arr.min())


def np_variance(values: Iterable[float], ddof: int = 1) -> float:
    """Return the (sample or population) variance of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(arr.var(ddof=ddof))


def np_std(values: Iterable[float], ddof: int = 1) -> float:
    """Return the standard deviation of *values* using NumPy."""

    arr = _to_ndarray(values)
    return float(arr.std(ddof=ddof))


def np_quantile(values: Iterable[float], q: float) -> float:
    """Return the q-quantile of *values* using NumPy's ``quantile``."""

    if not 0.0 <= q <= 1.0:
        raise ValueError("q must be between 0 and 1 inclusive.")
    arr = _to_ndarray(values)
    return float(np.quantile(arr, q))


def np_iqr(values: Iterable[float]) -> float:
    """Return the interquartile range (IQR) of *values* using NumPy."""

    arr = _to_ndarray(values)
    q1, q3 = np.quantile(arr, [0.25, 0.75])
    return float(q3 - q1)


def np_covariance(x: Iterable[float], y: Iterable[float], ddof: int = 1) -> float:
    """Return the covariance between *x* and *y* using NumPy."""

    x_arr = _to_ndarray(x)
    y_arr = _to_ndarray(y)
    if x_arr.size != y_arr.size:
        raise ValueError("x and y must contain the same number of elements.")
    cov_matrix = np.cov(x_arr, y_arr, ddof=ddof)
    return float(cov_matrix[0, 1])


def np_correlation(x: Iterable[float], y: Iterable[float]) -> float:
    """Return the Pearson correlation coefficient between *x* and *y*."""

    x_arr = _to_ndarray(x)
    y_arr = _to_ndarray(y)
    if x_arr.size != y_arr.size:
        raise ValueError("x and y must contain the same number of elements.")
    corr_matrix = np.corrcoef(x_arr, y_arr)
    return float(corr_matrix[0, 1])


def np_summary(values: Iterable[float]) -> Dict[str, float]:
    """Return a dictionary with common numerical summaries via NumPy.

    Mirrors :func:`pure_python_stats.summary` but uses NumPy under the hood.
    """

    arr = _to_ndarray(values)
    q25, q50, q75 = np.quantile(arr, [0.25, 0.5, 0.75])
    return {
        "count": float(arr.size),
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=1)),
        "min": float(arr.min()),
        "q25": float(q25),
        "median": float(q50),
        "q75": float(q75),
        "max": float(arr.max()),
        "iqr": float(q75 - q25),
        "range": float(arr.max() - arr.min()),
    }


__all__ = [
    "np_mean",
    "np_median",
    "np_min",
    "np_max",
    "np_range",
    "np_variance",
    "np_std",
    "np_quantile",
    "np_iqr",
    "np_covariance",
    "np_correlation",
    "np_summary",
]
