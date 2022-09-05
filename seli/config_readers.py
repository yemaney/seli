"""Collection of functions related to loading relevant config files.
"""

import json
from dataclasses import dataclass, field
from typing import Generator

from seli.logging_helper import get_logger

logger = get_logger(__name__)


@dataclass
class Configs:
    """
    Represents the configuration needed to complete a seli job.
    """

    job: dict[str, str]
    secrets: dict[str, str] = field(default_factory=dict, repr=False)


def read_configs(jobs_path: str, secrets_path: str) -> Generator[Configs, None, None]:
    """
    Read JSON config  files for jobs and secrets and generate Configs
    dataclasses.

    Parameters
    ----------
    jobs_path : str
        path to jobs JSON config file
    secrets_path : str
        path to secrets config file if it exists

    Yields
    ------
    Generator[Configs, None, None]
        Configs dataclasses

    Raises
    ------
    ValueError
        if the jobs JSON file doesn't have a `jobs` key
    """
    with open(jobs_path) as fp:
        jobs = json.load(fp)
        logger.info("job config found")

    if jobs.get("jobs") is None:
        logger.error("No jobs found : Check if input has a 'jobs' key")
        raise ValueError("No jobs found : Check if input has a 'jobs' key")

    secrets = None
    if secrets_path:
        with open(secrets_path) as fp:
            secrets = json.load(fp)
            logger.info("secrets config found")

    for job in jobs.get("jobs"):
        config_fields = {"job": job}
        if secrets is not None:
            config_fields["secrets"] = secrets

        yield Configs(**config_fields)
