#!/usr/bin/env python
from . import run


def main(*args, **kwargs):
    suite, errors = run.run(*args, **kwargs)
    results = run.parse_results(suite, errors)
    print(results)
