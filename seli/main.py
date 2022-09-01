"""Main module that orchestrates the execution of the seli workflow.
"""

import sys

from seli.config_readers import read_jobs
from seli.workers import get_worker


def main():
    """
    Main function of the package. Reads the jobs, and executes them
    with the appropriate worker function.
    """
    jobs_filepath = sys.argv[1]
    jobs = read_jobs(jobs_filepath)

    for job in jobs:
        worker = get_worker(job)
        worker(job)


if __name__ == "__main__":
    main()
