from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    def __init__(self,driver):
        self.driver = driver

    def payment_page(self,card_no,MM_YY,cvv):

        iframe = self.driver.find_element(By.ID, "headersFrame")
        self.driver.switch_to.frame(iframe)

        created_card = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//p[text()='Credit and Debit Cards']"))
        )
        created_card.click()

        card_number = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='cardNumber']"))
        )
        card_number.send_keys(card_no)

        month_and_year = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='cardExpirationMonth']"))
        )
        month_and_year.send_keys(MM_YY)

        cvv1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='cvv']"))
        )
        cvv1.send_keys(cvv)

    def payment_securely(self):
        pay_sec = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[starts-with(@class,'ptm-custom-btn ptm-hvr')])[1]"))
        )
        pay_sec.click()






