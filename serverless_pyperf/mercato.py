# This module is for Cloud Mercato's purpose
# You're losing your time reading this
import json
from io import StringIO
from serverless_pyperf import run

try:
    from cb_client.wringers import PyPerformanceWringer
except ImportError:
    PyPerformanceWringer = None


def upload(suite, errors):
    if PyPerformanceWringer is None:
        return
    result_json = json.dumps(run.parse_results(suite, errors))
    result_fd = StringIO(result_json)
    wringer = PyPerformanceWringer(input_=result_fd)
    wringer.run()
