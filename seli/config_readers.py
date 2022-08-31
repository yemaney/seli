import json


def read_jobs(input) -> list[dict[str, str]]:
    """
    Read a json file containing jobs that will be executed by
    seli workers.

    Parameters
    ----------
    input : str
        filepath to jobs json file

    Returns
    -------
    list[dict[str, str]]
        list of jobs that will be executed

    Raises
    ------
    ValueError
        if the jobs json file doesn't have a 'jobs' key
    """
    with open(input) as fp:
        jobs = json.load(fp)

    if jobs.get("jobs") is None:
        raise ValueError("No jobs found : Check if the input has a 'jobs' key")
    return jobs["jobs"]
