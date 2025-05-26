import sys
import json
import argparse
from serverless_pyperf import run

BENCHMARK_NAMES = [b.name for b in run.BENCHMARKS]


def main(**options):
    parser = argparse.ArgumentParser()

    parser.add_argument('benchmark_names', nargs='*', default='2to3', choices=BENCHMARK_NAMES)
    parser.add_argument('-r', '--rigorous', action='store_true')
    parser.add_argument('-f', '--fast', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-m', '--track-memory', action='store_true')
    parser.add_argument('--affinity', default=None)
    parser.add_argument('--min-time', default=None, type=int)
    parser.add_argument('--same-loops', default=None, type=int)
    parser.add_argument('--timeout', default=None, type=int)
    parser.add_argument('-u', '--unique-venvs', action='store_true')
    parser.add_argument('-p', '--python', default=None)
    parser.add_argument('-o', '--output', default=None)

    options = parser.parse_args()

    suite, errors = run.run(
        benchmark_names=options.benchmark_names,
        same_loops=options.same_loops,
        inherit_environ=None,
        debug_single_value=False,
        rigorous=options.rigorous,
        fast=options.fast,
        verbose=options.verbose,
        affinity=options.affinity,
        track_memory=options.track_memory,
        min_time=options.min_time,
        timeout=options.timeout,
        hook=[],
        unique_venvs=options.unique_venvs,
    )

    if errors:
        print(errors)

    results = run.parse_results(suite, errors)
    fd = open(options.output, 'w') if options.output else sys.stdout
    fd.write(json.dumps(results))


if __name__ == '__main__':
    main()
