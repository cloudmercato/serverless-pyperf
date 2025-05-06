#!/usr/bin/env python
import unittest
from serverless_pyperf import run


class RunTest(unittest.TestCase):
    def test_run(self):
        suite, errors = run.run(
            benchmark_names=['argparse'],
        )
        results = run.parse_results(suite, errors)
        print(results)


if __name__ == '__main__':
    unittest.main()
