"""Collection of functions related to loading relevant config files.
"""

import json
import sys
from dataclasses import dataclass, field
from typing import Generator

from seli.logging_helper import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class Configs:
    """
    Represents the configuration needed to complete a seli job.
    """

    job: dict[str, str]
    secrets: dict[str, str] = field(default_factory=dict, repr=False)


def read_configs(args: list[str]) -> Generator[Configs, None, None]:
    """
    Read JSON config  files for jobs and secrets and generate Configs
    dataclasses.

    Parameters
    ----------
    args : list[str]
        list with path to jobs JSON config file and secrets config if
        it exists

    Yields
    ------
    Generator[Configs, None, None]
        Configs dataclasses

    Raises
    ------
    ValueError
        if the jobs JSON file doesn't have a `jobs` key
    """
    with open(args[1]) as fp:
        jobs = json.load(fp)
        logger.info("job config found")

    if jobs.get("jobs") is None:
        logger.error("No jobs found : Check if input has a 'jobs' key")
        raise ValueError("No jobs found : Check if input has a 'jobs' key")

    secrets = None
    if len(args) > 2:
        with open(args[2]) as fp:
            secrets = json.load(fp)
            logger.info("secrets config found")

    for job in jobs.get("jobs"):
        config_fields = {"job": job}
        if secrets is not None:
            config_fields["secrets"] = secrets

        yield Configs(**config_fields)


def read_args() -> list[str]:
    """simple helper function to read sys args"""
    logger.info("reading sys.argv")
    return sys.argv
