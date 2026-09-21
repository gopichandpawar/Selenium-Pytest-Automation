from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.bus_search_locator import BusSearchLocator

class BusSearchPage:
    def __init__(self,driver):
        self.driver = driver

    def Bus_Search(self,from_city,to_city):
        #--------------------------From--------------------------
        from_input = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,BusSearchLocator.FROM_INPUT))
        )
        from_input.clear()
        from_input.send_keys(from_city)

        from_suggest_input = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,BusSearchLocator.FROM_SUGGEST_INPUT))
        )
        from_suggest_input.click()

        to_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, BusSearchLocator.TO_INPUT))
        )
        to_input.clear()
        to_input.send_keys(to_city)

        to_suggest_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, BusSearchLocator.TO_SUGGEST_INPUT))
        )
        to_suggest_input.click()

        search = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, BusSearchLocator.SEARCH_BUS))
        )
        search.click()



