from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.payment_locators import PaymentLocators

class PaymentPage:
    def __init__(self,driver):
        self.driver = driver

    def payment_details(self,card):
        debit_card = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,PaymentLocators.DEBIT_CARD))
        )
        debit_card.click()

        card_number = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, PaymentLocators.CARD_NUMBER))
        )
        card_number.send_keys(card['card_number'])

        name_on_card = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, PaymentLocators.NAME_ON_CARD))
        )
        name_on_card.send_keys(card['card_name'])

        expire_month = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, PaymentLocators.EXPIRE_MONTH))
        )
        expire_month.send_keys(card['expiry'])

        cvv = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, PaymentLocators.CVV))
        )
        cvv.send_keys(card['cvv'])

        continue1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, PaymentLocators.CONTINUE1))
        )
        continue1.click()

