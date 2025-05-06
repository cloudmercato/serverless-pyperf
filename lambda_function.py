import json
from io import StringIO

from serverless_pyperf import run
from cb_client.wringers import PyPerformanceWringer


def lambda_handler(event, context):
    benchmark_names = [b.name for b in run.BENCHMARKS]
    if event.get('benchmarks'):
        benchmark_names = [
            b for b in benchmark_names
            if b in event['benchmarks']
        ]

    suite, errors = run.run(
        benchmark_names=benchmark_names,
        same_loops=None,
        inherit_environ=None,
        debug_single_value=False,
        rigorous=event.get('rigorous', False),
        fast=event.get('fast', False),
        verbose=event.get('verbose', False),
        affinity=event.get('affinity'),
        track_memory=event.get('track_memory'),
        min_time=event.get('min_time'),
        timeout=event.get('timeout'),
        hook=[],
    )

    if errors:
        print(errors)

    result_json = json.dumps(run.parse_results(suite, errors))

    result_fd = StringIO(result_json)
    wringer = PyPerformanceWringer(input_=result_fd)
    wringer.run()


if __name__ == '__main__':
    event = {
        'benchmarks': ['argparse'],
    }
    context = {}
    lambda_handler(event, context)
