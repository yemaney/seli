from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def browser_worker(label: str):
    browser.get(label)


def button_worker(label: str):
    button = browser.find_element(By.XPATH, label)
    button.click()
