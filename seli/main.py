"""Main module that orchestrates the execution of the seli workflow.
"""

from seli.config_readers import read_args, read_configs
from seli.workers import get_worker


def main():
    """
    Main function of the package. Reads the jobs, and executes them
    with the appropriate worker function.
    """
    args = read_args()

    for job in read_configs(args):
        worker = get_worker(job)
        worker(job)


if __name__ == "__main__":
    main()
