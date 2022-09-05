import json
import os

import pytest

from seli import __version__
from seli.config_readers import read_configs


def test_version():
    assert __version__ == "2.0.0"


def test_read_jobs_fails():
    test_file = "input.json"
    with open(test_file, "w") as fp:
        json.dump(
            {"wrong_key": [{"kind": "browser", "label": "google"}]},
            fp,
        )

    with pytest.raises(
        ValueError, match="No jobs found : Check if input has a 'jobs' key"
    ):
        next(read_configs(jobs_path="input.json", secrets_path=""))

    os.remove(test_file)
