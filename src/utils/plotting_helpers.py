"""Plotting utilities for visualizing simulation results.

These helpers are thin wrappers around matplotlib / seaborn and are
primarily intended for interactive use in notebooks. They do not return
figures by default to keep the API simple; if you need programmatic
access, you can easily adapt or extend these functions.
"""

from __future__ import annotations

from typing import Iterable, Optional, Sequence

import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(
    values: Iterable[float],
    bins: int = 30,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    density: bool = False,
    alpha: float = 0.7,
    color: str | None = None,
) -> None:
    """Plot a simple histogram of *values*.

    Parameters
    ----------
    values:
        Iterable of numeric values to be histogrammed.
    bins:
        Number of bins or a bin specification accepted by matplotlib.
    title, xlabel, ylabel:
        Optional axis labels and title.
    density:
        If ``True``, plot a density histogram (area sums to 1).
    alpha:
        Transparency level for the bars.
    color:
        Optional color for the bars. If omitted, seaborn / matplotlib
        defaults are used.
    """

    data = list(values)
    if not data:
        raise ValueError("plot_histogram received an empty sequence.")

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, density=density, alpha=alpha, color=color)

    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    plt.tight_layout()
    plt.show()


def plot_line_with_ci(
    x: Sequence[float],
    y: Sequence[float],
    y_lower: Optional[Sequence[float]] = None,
    y_upper: Optional[Sequence[float]] = None,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    x_log: bool = False,
) -> None:
    """Plot a line with optional vertical confidence interval band.

    Parameters
    ----------
    x:
        Sequence of x-values.
    y:
        Sequence of y-values, same length as *x*.
    y_lower, y_upper:
        Optional sequences defining a band around *y*. If provided, both
        must be the same length as *x* and *y*.
    x_log:
        If ``True``, use a logarithmic scale on the x-axis.
    """

    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")

    if y_lower is not None or y_upper is not None:
        if y_lower is None or y_upper is None:
            raise ValueError("Both y_lower and y_upper must be provided or neither.")
        if len(y_lower) != len(x) or len(y_upper) != len(x):
            raise ValueError("y_lower and y_upper must match the length of x and y.")

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))

    plt.plot(x, y, marker="o", label="estimate")

    if y_lower is not None and y_upper is not None:
        plt.fill_between(x, y_lower, y_upper, color="gray", alpha=0.2, label="CI band")

    if x_log:
        plt.xscale("log")

    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    if y_lower is not None and y_upper is not None:
        plt.legend()

    plt.tight_layout()
    plt.show()


__all__ = [
    "plot_histogram",
    "plot_line_with_ci",
]
