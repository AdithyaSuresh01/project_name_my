"""Pure-Python implementations of basic numerical summary statistics.

The functions in this module are intentionally implemented without relying
on NumPy so that the underlying algorithms remain transparent and easy to
understand for educational purposes.

All functions accept any *iterable* of numbers; internally values are
materialized as a list to support multiple passes when needed.

Design notes
------------
- Functions raise ``ValueError`` when called with an empty iterable.
- Missing values (``None`` or ``float('nan')``) are **not** automatically
  filtered; callers should clean their data beforehand if needed.
- The implementations are not optimized for very large datasets; they are
  aimed at clarity rather than performance.
"""

from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple, Dict


def _to_list(values: Iterable[float]) -> List[float]:
    """Convert *values* to a list and validate non-emptiness.

    Parameters
    ----------
    values:
        Any iterable of numeric values.

    Returns
    -------
    list of float
        The values as a concrete list.

    Raises
    ------
    ValueError
        If *values* is empty.
    """

    data = list(values)
    if not data:
        raise ValueError("Cannot compute statistic on an empty sequence.")
    return data


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of *values*.

    Implementation uses a single pass accumulation and division by the
    number of observations.
    """

    data = _to_list(values)
    total = 0.0
    for x in data:
        total += x
    return total / len(data)


def median(values: Iterable[float]) -> float:
    """Return the median of *values*.

    For an odd number of observations, the middle value is returned.
    For an even number of observations, the average of the two middle
    values is returned.
    """

    data = sorted(_to_list(values))
    n = len(data)
    mid = n // 2

    if n % 2 == 1:  # odd
        return data[mid]
    # even
    return (data[mid - 1] + data[mid]) / 2.0


def minimum(values: Iterable[float]) -> float:
    """Return the minimum value in *values*.

    Equivalent to the built-in :func:`min`, but with consistent error
    messaging for empty input.
    """

    data = _to_list(values)
    m = data
    for x in data[1:]:
        if x < m:
            m = x
    return m


def maximum(values: Iterable[float]) -> float:
    """Return the maximum value in *values*.

    Equivalent to the built-in :func:`max`, but with consistent error
    messaging for empty input.
    """

    data = _to_list(values)
    m = data
    for x in data[1:]:
        if x > m:
            m = x
    return m


def data_range(values: Iterable[float]) -> float:
    """Return the range (max - min) of *values*."""

    data = _to_list(values)
    return maximum(data) - minimum(data)


def variance(values: Iterable[float], ddof: int = 1) -> float:
    """Return the sample or population variance of *values*.

    Parameters
    ----------
    values:
        Iterable of numeric observations.
    ddof:
        Delta degrees of freedom. ``ddof=1`` yields the *sample* variance
        (dividing by ``n - 1``); ``ddof=0`` yields the *population* variance
        (dividing by ``n``).

    Raises
    ------
    ValueError
        If there are fewer than ``ddof + 1`` observations.
    """

    data = _to_list(values)
    n = len(data)
    if n <= ddof:
        raise ValueError(
            f"variance requires at least {ddof + 1} data points, got {n}."
        )

    m = mean(data)
    acc = 0.0
    for x in data:
        diff = x - m
        acc += diff * diff
    return acc / (n - ddof)


def std_dev(values: Iterable[float], ddof: int = 1) -> float:
    """Return the standard deviation of *values*.

    This is simply the square root of :func:`variance`.
    """

    from math import sqrt

    return sqrt(variance(values, ddof=ddof))


def quantile(values: Iterable[float], q: float) -> float:
    """Return the *q*-quantile of *values* using linear interpolation.

    Parameters
    ----------
    values:
        Iterable of numeric observations.
    q:
        Quantile in the closed interval [0, 1]. For example, ``q=0.5``
        yields the median.

    Notes
    -----
    This implementation follows a simple linear interpolation between
    sorted data points, similar to NumPy's ``method='linear'`` for
    :func:`numpy.quantile`.
    """

    if not 0.0 <= q <= 1.0:
        raise ValueError("q must be between 0 and 1 inclusive.")

    data = sorted(_to_list(values))
    n = len(data)
    if n == 1:
        return data

    pos = q * (n - 1)
    lower_index = int(pos)
    upper_index = min(lower_index + 1, n - 1)
    weight = pos - lower_index

    lower = data[lower_index]
    upper = data[upper_index]

    return lower * (1.0 - weight) + upper * weight


def iqr(values: Iterable[float]) -> float:
    """Return the interquartile range (IQR = Q3 - Q1) of *values*."""

    data = _to_list(values)
    q1 = quantile(data, 0.25)
    q3 = quantile(data, 0.75)
    return q3 - q1


def covariance(x: Iterable[float], y: Iterable[float], ddof: int = 1) -> float:
    """Return the (sample or population) covariance between *x* and *y*.

    Parameters
    ----------
    x, y:
        Iterables representing paired observations. Must be of equal
        length after materialization.
    ddof:
        Delta degrees of freedom. ``ddof=1`` gives the *sample* covariance.

    Raises
    ------
    ValueError
        If the sequences are of differing length, empty, or too short
        given ``ddof``.
    """

    x_list = _to_list(x)
    y_list = _to_list(y)

    if len(x_list) != len(y_list):
        raise ValueError("x and y must contain the same number of elements.")

    n = len(x_list)
    if n <= ddof:
        raise ValueError(
            f"covariance requires at least {ddof + 1} paired values, got {n}."
        )

    mx = mean(x_list)
    my = mean(y_list)

    acc = 0.0
    for xi, yi in zip(x_list, y_list):
        acc += (xi - mx) * (yi - my)

    return acc / (n - ddof)


def correlation(x: Iterable[float], y: Iterable[float]) -> float:
    """Return the Pearson correlation coefficient between *x* and *y*.

    The coefficient lies in the interval [-1, 1] in typical cases.
    """

    from math import sqrt

    cov = covariance(x, y, ddof=1)
    sx = std_dev(x, ddof=1)
    sy = std_dev(y, ddof=1)
    if sx == 0 or sy == 0:
        raise ValueError("Correlation is undefined when one series has zero variance.")
    return cov / (sx * sy)


def summary(values: Iterable[float]) -> Dict[str, float]:
    """Return a dictionary with common numerical summaries for *values*.

    The returned dictionary contains:

    - ``count``
    - ``mean``
    - ``std`` (sample standard deviation, ddof=1)
    - ``min``
    - ``q25``
    - ``median``
    - ``q75``
    - ``max``
    - ``iqr``
    - ``range``
    """

    data = _to_list(values)
    return {
        "count": float(len(data)),
        "mean": mean(data),
        "std": std_dev(data, ddof=1),
        "min": minimum(data),
        "q25": quantile(data, 0.25),
        "median": median(data),
        "q75": quantile(data, 0.75),
        "max": maximum(data),
        "iqr": iqr(data),
        "range": data_range(data),
    }


__all__ = [
    "mean",
    "median",
    "minimum",
    "maximum",
    "data_range",
    "variance",
    "std_dev",
    "quantile",
    "iqr",
    "covariance",
    "correlation",
    "summary",
]
