"""Simulation helpers for exploring sampling distributions of statistics.

The core idea is to provide a small, composable API around the repeated
sampling pattern that often appears in introductory statistics:

1. Draw a random sample of size *n* from some distribution.
2. Compute a statistic (e.g., mean, median, variance) on that sample.
3. Repeat many times and inspect the distribution of the statistic.

This module is distribution-agnostic: callers supply a *sample generator*
function and a *statistic* function. This keeps the API flexible and easy
to integrate with arbitrary data-generating processes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, List, Dict, Any

from .pure_python_stats import summary as summary_fn


StatisticFunc = Callable[[Iterable[float]], float]
SampleGenerator = Callable[[int], Iterable[float]]


@dataclass
class SimulationResult:
    """Container for the results of a simulation run.

    Attributes
    ----------
    values:
        List of simulated statistic values, one per simulation.
    statistic_name:
        A human-readable name for the statistic (e.g., "mean").
    sample_size:
        The size of each random sample (n).
    n_simulations:
        Number of repeated simulations.
    summary:
        A dictionary with descriptive statistics of ``values`` as
        computed by :func:`pure_python_stats.summary`.
    metadata:
        Optional free-form metadata (e.g., distribution parameters).
    """

    values: List[float]
    statistic_name: str
    sample_size: int
    n_simulations: int
    summary: Dict[str, float]
    metadata: Dict[str, Any] | None = None


def run_statistic_simulation(
    sample_generator: SampleGenerator,
    statistic: StatisticFunc,
    sample_size: int,
    n_simulations: int,
    statistic_name: str | None = None,
    metadata: Dict[str, Any] | None = None,
) -> SimulationResult:
    """Run repeated simulations of a statistic on random samples.

    Parameters
    ----------
    sample_generator:
        A callable ``sample_generator(n) -> Iterable[float]`` that returns
        a collection of *n* observations drawn from some distribution.
    statistic:
        A callable ``statistic(values) -> float`` that computes a scalar
        summary from an iterable of numbers.
    sample_size:
        The size ``n`` of each simulated sample.
    n_simulations:
        The number of repeated simulations to perform.
    statistic_name:
        Optional label used for reporting and plotting. If not provided,
        ``statistic.__name__`` is used when available.
    metadata:
        Optional dictionary with extra metadata to be attached to the
        resulting :class:`SimulationResult`.

    Returns
    -------
    SimulationResult
        Object containing the sequence of simulated statistic values and
        a summary.
    """

    if sample_size <= 0:
        raise ValueError("sample_size must be positive.")
    if n_simulations <= 0:
        raise ValueError("n_simulations must be positive.")

    stat_name = statistic_name or getattr(statistic, "__name__", "statistic")

    values: List[float] = []
    for _ in range(n_simulations):
        sample = sample_generator(sample_size)
        # Materialize in case the generator is single-use
        sample_list = list(sample)
        if len(sample_list) != sample_size:
            raise ValueError(
                f"sample_generator returned {len(sample_list)} observations, "
                f"expected {sample_size}."
            )
        value = statistic(sample_list)
        values.append(float(value))

    sim_summary = summary_fn(values)

    return SimulationResult(
        values=values,
        statistic_name=stat_name,
        sample_size=sample_size,
        n_simulations=n_simulations,
        summary=sim_summary,
        metadata=metadata or {},
    )


__all__ = [
    "SimulationResult",
    "run_statistic_simulation",
]
