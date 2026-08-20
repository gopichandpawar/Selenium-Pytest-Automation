from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.practice_locators import PracticeLocators

class PracticePage:
    def __init__(self,driver):
        self.driver = driver

    def Pactice_Page(self):
        start_practice = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,PracticeLocators.STARTS_PRACTICE))
        )
        start_practice.click()

        shop_now = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.ID,PracticeLocators.SHOP_NOW))
        )
        self.driver.execute_script("arguments[0].click();",shop_now)

