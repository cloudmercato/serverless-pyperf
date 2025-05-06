import unittest
from unittest.mock import patch
from pyperf import _bench
from serverless_pyperf import run


class RunTest(unittest.TestCase):
    @patch('serverless_pyperf.run.run_benchmarks', return_value=(None, None))
    def test_run(self, mock_run_benchmarks):
        suite, errors = run.run(
            benchmark_names=['argparse'],
        )


class ParseResultsTest(unittest.TestCase):
    def test_parse(self):
        suite = _bench.BenchmarkSuite(
            benchmarks=[
                _bench.Benchmark([_bench.Run(
                    values=(.1, .2, .3),
                    metadata={'name': 'foo'},
                )]),
            ]
        )
        results = run.parse_results(suite, None)
        self.assertIsInstance(results, dict)


if __name__ == '__main__':
    unittest.main()
