import sys

from seli.config_readers import read_jobs


def main():
    jobs_filepath = sys.argv[1]
    read_jobs(jobs_filepath)


if __name__ == "__main__":
    main()
