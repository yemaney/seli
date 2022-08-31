import sys

from seli.config_readers import read_jobs
from seli.workers import browser_worker


def main():
    jobs_filepath = sys.argv[1]
    jobs = read_jobs(jobs_filepath)

    for job in jobs:
        if job["kind"] == "browser":
            browser_worker(job["label"])


if __name__ == "__main__":
    main()
