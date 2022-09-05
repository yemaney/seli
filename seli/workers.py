"""Collection of workers, with related functions and data structures.

Each worker worker takes a job description json as an input, and uses it
to perform a selenium task.

`WORKERS` is a dictionary that maps `kind` keys to the corresponding
worker function.

`get_worker` is the function in charge of selecting the appropriate
worker for a job. The only function to be imported into the main
module.
"""

import functools
from typing import Callable, Protocol

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from seli.logging_helper import get_logger

logger = get_logger(__name__)


class ConfigInput(Protocol):
    job: dict[str, str]
    secrets: dict[str, str]


worker = Callable[[ConfigInput, WebDriver], None]


def start_browser() -> WebDriver:
    """Start Chrome Browser Session"""
    return webdriver.Chrome(ChromeDriverManager().install())


def log_worker(func: worker) -> worker:
    """
    Utility decorator function to add consistent logging behavior to
    worker functions.

    Parameters
    ----------
    func : worker
        a worker function

    Returns
    -------
    worker
        same worker function passed but with logging enabled
    """

    @functools.wraps(func)
    def inner(config_input: ConfigInput, browser: WebDriver) -> None:

        if config_input.job.get("url") is not None:
            info = config_input.job["url"]
        else:
            info = config_input.job["xpath"]

        logger.info(f"{func.__name__} at {info}")
        res = func(config_input, browser)
        return res

    return inner


@log_worker
def browser_worker(config_input: ConfigInput, browser: WebDriver) -> None:
    """
    Browses to a particular url.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.
    browser: WebDriver
        selenium webdriver connected to a browser session
    """
    browser.get(config_input.job["url"])


@log_worker
def button_worker(config_input: ConfigInput, browser: WebDriver) -> None:
    """
    Finds a button using an XPATH string and clicks it.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.
    browser: WebDriver
        selenium webdriver connected to a browser session
    """
    button = browser.find_element(By.XPATH, config_input.job["xpath"])
    button.click()


@log_worker
def field_worker(config_input: ConfigInput, browser: WebDriver) -> None:
    """
    Finds a text field using an XPATH and then enters text
    into the field.

    Parameters
    ----------
    config_input : ConfigInput
        Config dataclass with information to complete the job.
    browser: WebDriver
        selenium webdriver connected to a browser session
    """
    if config_input.job.get("secret"):
        keys = config_input.secrets[config_input.job["secret"]]
    else:
        keys = config_input.job["text"]

    button = browser.find_element(By.XPATH, config_input.job["xpath"])
    button.send_keys(keys)


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
