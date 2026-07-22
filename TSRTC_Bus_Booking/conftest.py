from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach",True)

    #lauching chrome and opening bus booking page
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tgsrtcbus.in/")

    yield driver