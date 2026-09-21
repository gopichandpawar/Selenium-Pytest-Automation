from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.payment_locator import PaymentLocator

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def Payment_Details(self):
        UPI_option = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, PaymentLocator.UPI_OPTION))
        )
        UPI_option.click()

        view_QR = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, PaymentLocator.VIEW_QR))
        )
        view_QR.click()
