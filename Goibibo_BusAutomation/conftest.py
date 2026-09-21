from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
@pytest.fixture(scope="class")
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.goibibo.com/bus/")

    yield driver