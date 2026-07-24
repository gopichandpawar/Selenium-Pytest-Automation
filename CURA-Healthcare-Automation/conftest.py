from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def driver():
    #setting chrome option
    options = Options()
    options.add_experimental_option("detach",True)

    #lauching chrome and opening Healthcare Page
    driver = webdriver.Chrome(options=options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    yield driver
