from serverless_pyperf import run, mercato


def handler(event, context):
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
    print(suite)
    print(errors)

    if errors:
        print(errors)
    mercato.upload(suite, errors)

    results = run.parse_results(suite, errors)
    return results


if __name__ == '__main__':
    event = {
        'benchmarks': ['argparse'],
    }
    context = {}
    handler(event, context)
