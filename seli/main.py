"""Main module that orchestrates the execution of the seli workflow.
"""

import typer

from seli.config_readers import read_configs
from seli.workers import get_worker, start_browser

app = typer.Typer()


@app.command()
def main(jobs: str, secrets: str = typer.Argument("")):
    """
    Main function of the package. Reads the jobs, and executes them
    with the appropriate worker function.

    Parameters
    ----------
    jobs : str
        path to jobs JSON config file
    secrets : str, optional
        path to the secrets config file, by default typer.Argument("")
    """

    browser = start_browser()
    for job in read_configs(jobs, secrets):
        worker = get_worker(job)
        worker(job, browser)
