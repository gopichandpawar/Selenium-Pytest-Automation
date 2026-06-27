from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    def __init__(self,driver):
        self.driver = driver

    def bank_management(self):
        bank_mng = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='manager()']"))
        )
        bank_mng.click()

    def add_customer(self,name1,last_name1,post_code1):
        add_ctm = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='addCust()']"))
        )
        add_ctm.click()

        name = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
        )
        name.send_keys(name1)

        last_name = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Last Name']"))
        )
        last_name.send_keys(last_name1)

        post_code = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Post Code']"))
        )
        post_code.send_keys(post_code1)

        add_customer1 = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        add_customer1.click()