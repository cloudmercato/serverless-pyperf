import json
from scw_serverless import Serverless
from serverless_pyperf import run, mercato

app = Serverless('pyperf')


@app.func()
def run_pyperf(options, _context):

    options = json.loads(options['body'])

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
    return {"statusCode": 200, "body": results}


if __name__ == "__main__":
    from scaleway_functions_python import local
    local.serve_handler(run_pyperf)
