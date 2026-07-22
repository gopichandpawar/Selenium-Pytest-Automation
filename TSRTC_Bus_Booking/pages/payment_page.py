from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    def __init__(self,driver):
        self.driver = driver

    def Payment_Details(self):
        payment_mode = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='radio']"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", payment_mode)
        self.driver.execute_script("arguments[0].click();", payment_mode)

        payment = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[@type='button'])[4]"))
        )
        payment.click()

        click_ok = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[@type='button'])[6]"))
        )
        click_ok.click()

        pay_securely = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div//button[starts-with(@class,'ptm-custom-btn')]"))
        )
        pay_securely.click()
