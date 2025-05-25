import os
import json
from serverless_pyperf import run, mercato

os.chdir('/tmp')


def handler(event, context):
    params = json.loads(event['body'])

    benchmark_names = [b.name for b in run.BENCHMARKS]
    if params.get('benchmarks'):
        benchmark_names = [
            b for b in benchmark_names
            if b in params['benchmarks']
        ]

    suite, errors = run.run(
        benchmark_names=benchmark_names,
        same_loops=None,
        inherit_environ=None,
        debug_single_value=False,
        rigorous=params.get('rigorous', False),
        fast=params.get('fast', False),
        verbose=params.get('verbose', False),
        affinity=params.get('affinity'),
        track_memory=params.get('track_memory'),
        min_time=params.get('min_time'),
        timeout=params.get('timeout'),
        hook=[],
        unique_venvs=params.get('unique_venvs', False),
    )

    if errors:
        print(errors)
    mercato.upload(suite, errors)

    results = run.parse_results(suite, errors)
    return {
        "statusCode": 200,
        "body": json.dumps(results),
    }


if __name__ == '__main__':
    event = {
        'body': json.dumps({'benchmarks': ['argparse']}),
    }
    context = {}
    handler(event, context)
