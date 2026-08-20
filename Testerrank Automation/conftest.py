from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach",True)

    #lauching chrome and open Testerrank Page
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.testerrank.com/practice")

    yield driver