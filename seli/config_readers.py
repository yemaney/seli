"""Collection of functions related to loading relevant config files.
"""

import json
import sys
from typing import Union


def read_configs(
    args: list[str],
) -> tuple[list[dict[str, str]], Union[dict[str, str], None]]:
    """
    Read a JSON config  file for either a jobs or credentials config.

    Parameters
    ----------
    file_path : str
        path to file being loaded
    kind : str, optional
        context of the config file, by default "jobs"

    Returns
    -------
    tuple[list[dict[str, str]],  dict[str, str] | None]
        Tuple of job dictionaries and dict of credentials if they exist

    Raises
    ------
    ValueError
        if the jobs JSON file doesn't have a `jobs` key
    """

    with open(args[1]) as fp:
        jobs = json.load(fp)

    if jobs.get("jobs") is None:
        raise ValueError("No jobs found : Check if the input has a 'jobs' key")

    credentials = None
    if len(args) > 2:
        with open(args[2]) as fp:
            credentials = json.load(fp)

    return jobs["jobs"], credentials


def read_args() -> list[str]:
    """simple helper function to read sys args"""
    return sys.argv
