from serverless_pyperf import run, mercato


def handler(request):
    options = request.get_json()
    benchmark_names = [b.name for b in run.BENCHMARKS]
    if options.get('benchmarks'):
        benchmark_names = [
            b for b in benchmark_names
            if b in options['benchmarks']
        ]

    suite, errors = run.run(
        benchmark_names=benchmark_names,
        same_loops=None,
        inherit_environ=None,
        debug_single_value=False,
        rigorous=options.get('rigorous', False),
        fast=options.get('fast', False),
        verbose=options.get('verbose', False),
        affinity=options.get('affinity'),
        track_memory=options.get('track_memory'),
        min_time=options.get('min_time'),
        timeout=options.get('timeout'),
        hook=[],
    )

    if errors:
        print(errors)
    mercato.upload(suite, errors)

    results = run.parse_results(suite, errors)
    return results
