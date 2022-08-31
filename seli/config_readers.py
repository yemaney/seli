import json


def read_jobs(jobs_filepath: str) -> list[dict[str, str]]:
    """
    Read a json file containing jobs that will be executed by
    seli workers.

    Parameters
    ----------
    jobs_filepath : str
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
    with open(jobs_filepath) as fp:
        jobs = json.load(fp)

    if jobs.get("jobs") is None:
        raise ValueError("No jobs found : Check if the input has a 'jobs' key")
    return jobs["jobs"]
