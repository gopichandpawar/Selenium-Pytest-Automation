from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.address_locators import AddressLocator
from selenium.webdriver.support.ui import Select

class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def address_detail(self,customer):
        full_name = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,AddressLocator.FULL_NAME))
        )
        full_name.send_keys(customer['full_name'])

        mobile = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.MOBILE))
        )
        mobile.send_keys(customer['mobile'])

        address = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.ADDRESS))
        )
        address.send_keys(customer['address'])

        landmark = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.LANDMARK))
        )
        landmark.send_keys(customer['landmark'])

        city = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.CITY))
        )
        city.send_keys(customer['city'])

        state = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.STATE))
        )
        select = Select(state)
        select.select_by_value("Punjab")

        pin_code =  WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.PIN_CODE))
        )
        pin_code.send_keys(customer['pincode'])

        save_address =  WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.SAVE_ADDRESS))
        )
        self.driver.execute_script("arguments[0].click();", save_address)

        continue1 =  WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, AddressLocator.CONTINUE))
        )
        self.driver.execute_script("arguments[0].click();", continue1)


