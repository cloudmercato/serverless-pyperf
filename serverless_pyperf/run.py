import sys
import argparse
from pyperformance._manifest import load_manifest
from pyperformance.run import run_benchmarks

manifest = load_manifest(None)
BENCHMARKS = [b for b in manifest.benchmarks]


def run(
    benchmark_names,
    same_loops=None,
    inherit_environ=None,
    debug_single_value=False,
    rigorous=False,
    fast=False,
    verbose=False,
    affinity=None,
    track_memory=None,
    min_time=None,
    timeout=None,
    hook=[],
    unique_venvs=False,
):
    benchmarks = [b for b in BENCHMARKS if b.name in benchmark_names]
    options = argparse.Namespace(
        same_loops=same_loops,
        inherit_environ=inherit_environ,
        debug_single_value=debug_single_value,
        rigorous=rigorous,
        fast=fast,
        verbose=verbose,
        affinity=affinity,
        track_memory=track_memory,
        min_time=min_time,
        timeout=timeout,
        hook=hook,
        unique_venvs=unique_venvs,
    )

    suite, errors = run_benchmarks(benchmarks, sys.executable, options)
    return suite, errors


def parse_results(suite, errors):
    results = {}
    metadata = suite.get_metadata()
    py_metadata = {
        k: v for b in suite._benchmarks
        for k, v in b.get_metadata().items()
        if k.startswith('python_')
    }
    for bench in suite._benchmarks:
        results[bench.get_name()] = {
            **metadata,
            **bench.get_metadata(),
            **py_metadata,
            'name': bench.get_name(),

            'loops': bench.get_loops(),
            'required_nprocesses': bench.required_nprocesses(),
            'total_duration': bench.get_total_duration(),

            'unit': bench.get_unit(),
            'mean': bench.mean(),
            'stdev': bench.stdev(),
            'median': bench.median(),
            'median_abs_dev': bench.median_abs_dev(),
            'perc5': bench.percentile(5),
            'perc95': bench.percentile(95),
        }
    return results
