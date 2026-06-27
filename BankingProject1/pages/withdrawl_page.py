from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WithdrawlPage:
    def __init__(self,driver):
        self.driver = driver

    def Withdrawl(self,amount1):
        with_page = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='withdrawl()']"))
        )
        with_page.click()

        amount = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//input[@placeholder='amount']"))
        )
        amount.send_keys(amount1)

        withdrawl = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))
        )
        withdrawl.click()