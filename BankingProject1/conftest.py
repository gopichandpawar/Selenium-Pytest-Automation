from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach",True)

    #lauching chrome and opening practice page
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/?utm_source=chatgpt.com#/login")

    yield driver





