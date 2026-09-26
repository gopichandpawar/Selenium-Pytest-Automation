from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.insurance_locators import InsuranceLocators
from selenium.webdriver.support.ui import Select

class InsurancePage:
    def __init__(self,driver):
        self.driver = driver

    def Insurance_Data(self,ins_data):
        name = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.NAME))
        )
        name.send_keys(ins_data['name1'])

        last_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.LAST_NAME))
        )
        last_name.send_keys(ins_data['last_name1'])

        date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.DATE))
        )
        date.send_keys(ins_data['date1'])

        gender = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.GENDER))
        )
        self.driver.execute_script("arguments[0].click();", gender)

        address = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, InsuranceLocators.ADDRESS))
        )
        address.send_keys(ins_data['address1'])

        country = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, InsuranceLocators.COUNTRY))
        )
        select = Select(country)
        select.select_by_value(ins_data['country1'])

        zip_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.ZIP_CODE))
        )
        zip_code.send_keys(ins_data['zip_code1'])

        city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.CITY))
        )
        city.send_keys(ins_data['city1'])

        occupation = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, InsuranceLocators.OCCUPATION))
        )
        select = Select(occupation)
        select.select_by_value(ins_data['occupation1'])

        hobby = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.HOBBY))
        )
        self.driver.execute_script("arguments[0].click();", hobby)

        website = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, InsuranceLocators.WEBSITE))
        )

        website.clear()
        website.send_keys(ins_data['website1'])

        picture = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, InsuranceLocators.PICTURE))
        )

        picture.send_keys(
            r"C:\Users\HP\Pictures\Camera Roll\car.jpg"
        )

        next1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InsuranceLocators.NEXT1))
        )
        next1.click()