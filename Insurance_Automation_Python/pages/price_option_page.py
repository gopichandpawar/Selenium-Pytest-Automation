from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.select_price_option import PriceOptionLocator

class PriceOptionPage:
    def __init__(self,driver):
        self.driver = driver

    def Price_Option_Data(self):
        select_silver = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, PriceOptionLocator.SELECT_SILVER))
        )
        self.driver.execute_script("arguments[0].click();", select_silver)

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

        next3 = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, PriceOptionLocator.NEXT3))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next3)
        next3.click()
