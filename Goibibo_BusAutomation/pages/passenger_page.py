from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.passenger_locator import PassengerLocator

class PassengerPage:
    def __init__(self,driver):
        self.driver = driver

    def Passenger_Details(self,data):

        radio_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.RADIO_BUTTON))
        )
        self.driver.execute_script("arguments[0].click();", radio_button)

        full_name = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,PassengerLocator.FULL_NAME))
        )
        full_name.send_keys(data['name'])

        age = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.AGE))
        )
        age.send_keys(data['age'])

        gender = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.GENDER))
        )
        gender.click()

        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.EMAIL))
        )
        email.send_keys(data['email'])

        number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.MOBILE))
        )
        number.send_keys(data['number'])

        billing_add = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.BILLING_ADDRESS))
        )
        billing_add.send_keys(data["billing_address"])

        pin_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.PIN_CODE))
        )
        pin_code.send_keys(data['pin_code'])

        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.CHECKBOX))
        )
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.driver.execute_script("window.scrollBy(0,1200);")

        pay = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PassengerLocator.PAY))
        )
        pay.click()