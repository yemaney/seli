from typing import Callable

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def browser_worker(job: dict[str, str]):
    browser.get(job["label"])


def button_worker(job: dict[str, str]):
    button = browser.find_element(By.XPATH, job["label"])
    button.click()


def field_worker(job: dict[str, str]):
    button = browser.find_element(By.XPATH, job["label"])
    button.send_keys(job["text"])


worker = Callable[[dict[str, str]], None]

WORKERS: dict[str, worker] = {
    "browser": browser_worker,
    "button": button_worker,
    "field": field_worker,
}


def get_worker(job: dict[str, str]) -> worker:
    return WORKERS[job["kind"]]
