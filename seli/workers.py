"""Collection of workers, with related functions and data structures.

Each worker worker takes a job description json as an input, and uses it
to perform a selenium task.

`WORKERS` is a dictionary that maps `kind` keys to the corresponding
worker function.

`get_worker` is the function in charge of selecting the appropriate
worker for a job. The only function to be imported into the main
module.
"""

from typing import Callable, Protocol

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


class ConfigInput(Protocol):
    job: dict[str, str]
    secrets: dict[str, str]


def browser_worker(config_input: ConfigInput):
    """
    Browses to a particular url.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.
    """
    browser.get(config_input.job["url"])


def button_worker(config_input: ConfigInput):
    """
    Finds a button using an XPATH string and clicks it.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.
    """
    button = browser.find_element(By.XPATH, config_input.job["xpath"])
    button.click()


def field_worker(config_input: ConfigInput):
    """
    Finds a text field using an XPATH and then enters text
    into the field.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.
    """
    if config_input.job.get("secret"):
        keys = config_input.secrets[config_input.job["secret"]]
    else:
        keys = config_input.job["text"]

    button = browser.find_element(By.XPATH, config_input.job["xpath"])
    button.send_keys(keys)


worker = Callable[[ConfigInput], None]

WORKERS: dict[str, worker] = {
    "browser": browser_worker,
    "button": button_worker,
    "field": field_worker,
}


def get_worker(config_input: ConfigInput) -> worker:
    """
    Given a job definition, select the appropriate worker function.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.

    Returns
    -------
    worker
        The appropriate worker function given the `kind` field in the
        input dictionary defining a job.
    """
    return WORKERS[config_input.job["kind"]]
