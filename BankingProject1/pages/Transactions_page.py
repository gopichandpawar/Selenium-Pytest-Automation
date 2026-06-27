from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransactionsPage:
    def __init__(self,driver):
        self.driver = driver

    def transaction_page(self):
        tran_his = WebDriverWait(self.driver,15).until(
        EC.element_to_be_clickable((By.XPATH,"//button[@ng-click='transactions()']"))
        )
        tran_his.click()
