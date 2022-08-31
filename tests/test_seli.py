import json
import os

import pytest

from seli import __version__
from seli.config_readers import read_jobs


def test_version():
    assert __version__ == "0.1.0"


def test_read_jobs_fails():
    test_file = "input.json"
    with open(test_file, "w") as fp:
        json.dump(
            {"wrong_key": [{"kind": "browser", "label": "google"}]},
            fp,
        )

    with pytest.raises(
        ValueError, match="No jobs found : Check if the input has a 'jobs' key"
    ):
        read_jobs(test_file)

    os.remove(test_file)
