import sys

from seli.config_readers import read_jobs
from seli.workers import get_worker


def main():
    jobs_filepath = sys.argv[1]
    jobs = read_jobs(jobs_filepath)

    for job in jobs:
        worker = get_worker(job)
        worker(job)


if __name__ == "__main__":
    main()
