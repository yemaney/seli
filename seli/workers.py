"""Collection of workers, with related functions and data structures.

Each worker worker takes a job description json as an input, and uses it
to perform a selenium task.

`WORKERS` is a dictionary that maps `kind` keys to the corresponding
worker function.

`get_worker` is the function in charge of selecting the appropriate
worker for a job. The only function to be imported into the main
module.
"""

from typing import Callable

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def browser_worker(job: dict[str, str]):
    """
    Browses to a particular url.

    Parameters
    ----------
    job : dict[str, str]
        dictionary defining the browser worker. In the format
        `of {"kind" : "browser", "url": "http://google.com"}`
    """
    browser.get(job["url"])


def button_worker(job: dict[str, str]):
    """
    Finds a button using an XPATH string and clicks it.

    Parameters
    ----------
    job : dict[str, str]
        dictionary defining the browser worker. In the format
        `{"kind" : "button", "xpath" : "/html/button"}`
    """
    button = browser.find_element(By.XPATH, job["xpath"])
    button.click()


def field_worker(job: dict[str, str]):
    """
    Finds a text field using an XPATH and then enters text
    into the field.

    Parameters
    ----------
    job : dict[str, str]
        dictionary defining the field worker. In the format
        `{"kind" : "field", "xpath" : "/html/enter",
        "text": "username"}`
    """
    button = browser.find_element(By.XPATH, job["xpath"])
    button.send_keys(job["text"])


worker = Callable[[dict[str, str]], None]

WORKERS: dict[str, worker] = {
    "browser": browser_worker,
    "button": button_worker,
    "field": field_worker,
}


def get_worker(job: dict[str, str]) -> worker:
    """
    Given a job definition, select the appropriate worker function.

    Parameters
    ----------
    job : dict[str, str]
        dictionary defining a worker function that is present in the
        WORKERS dictionary.

    Returns
    -------
    worker
        The appropriate worker function given the `kind` field in the
        input dictionary defining a job.
    """
    return WORKERS[job["kind"]]
