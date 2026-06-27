from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Customers:
    def __init__(self,driver):
        self.driver = driver

    def bank_management(self):
        bank_mng = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='manager()']"))
        )
        bank_mng.click()

    def customer(self):
        cust_detail = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='showCust()']"))
        )
        cust_detail.click()

    def search_customer(self,customer_name):
        search = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search Customer']"))
        )
        search.send_keys(customer_name)

    def delete_customer(self):
        delete = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete']"))
        )
        delete.click()