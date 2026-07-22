from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PassengerPage:
    def __init__(self,driver):
        self.driver = driver

    def passenger_details(self):
        # ____________________________ Passenger Details ___________________________
        try:
            gender = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    ".ant-select-selector"
                ))
            )
            gender.click()

            male = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[@class='ant-select-item-option-content' and text()='Male']"
                ))
            )
            male.click()

        except Exception as e:
            print("it get a error", e)

        name = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name']"))
        )
        name.send_keys("Gopichand")

        age = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Age']"))
        )
        age.send_keys("24")

        email = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']"))
        )
        email.send_keys("gopichandpawar390@gmail.com")

        mobile = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Mobile']"))
        )
        mobile.send_keys("7499552687")

