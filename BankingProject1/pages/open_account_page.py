from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class OpenAccount:
    def __init__(self,driver):
        self.driver = driver

    def bank_management(self):
        bank_mng = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='manager()']"))
        )
        bank_mng.click()

    def open_account(self):
        add_ctm = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='openAccount()']"))
        )
        add_ctm.click()

        customer = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='userSelect']"))
        )
        select = Select(customer)
        select.select_by_visible_text("Ron Weasly")

        currency = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='currency']"))
        )
        select = Select(currency)
        select.select_by_visible_text("Pound")

        process = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        process.click()

