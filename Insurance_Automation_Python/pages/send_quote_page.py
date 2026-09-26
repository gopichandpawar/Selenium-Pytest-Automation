from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.send_quote_locators import SendQuoteLocators

class SendQuotePage:
    def __init__(self,driver):
        self.driver = driver

    def Send_Quote_data(self,quote_data):
        email = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,SendQuoteLocators.EMAIL))
        )
        email.send_keys(quote_data['email1'])

        phone = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,SendQuoteLocators.PHONE))
        )
        phone.send_keys(quote_data['phone1'])

        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendQuoteLocators.USERNAME))
        )
        username.send_keys(quote_data['username1'])

        password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendQuoteLocators.PASSWORD))
        )
        password.send_keys(quote_data['password1'])

        con_password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendQuoteLocators.CON_PASSWORD))
        )
        con_password.send_keys(quote_data['con_password1'])

        comment = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendQuoteLocators.COMMENTS))
        )
        comment.send_keys(quote_data['comment1'])

        send = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SendQuoteLocators.SEND))
        )
        send.click()