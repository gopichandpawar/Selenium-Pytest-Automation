from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.product_locators import ProductLocators
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self,driver):
        self.driver = driver

    def Product_Data(self,pro_data):
        start_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ProductLocators.START_DATE))
        )
        start_date.send_keys(pro_data['start_date1'])

        insurance_sum = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ProductLocators.INSURANCE_SUM))
        )
        select = Select(insurance_sum)
        select.select_by_value(pro_data['insurance_sum1'])

        merit_rating = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, ProductLocators.MERIT_RATING))
        )
        select = Select(merit_rating)
        select.select_by_value(pro_data['merit_rating1'])

        damage_ins = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ProductLocators.DAMAGE_INSURANCE))
        )
        select = Select(damage_ins)
        select.select_by_value(pro_data['damage_ins1'])

        euro_protection = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, ProductLocators.EURO_PROTECTION))
        )
        self.driver.execute_script("arguments[0].click();", euro_protection)

        courtesy_car = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ProductLocators.COURTESY_CAR))
        )
        select = Select(courtesy_car)
        select.select_by_value(pro_data['courtesy_car1'])

        next2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ProductLocators.NEXT2))
        )
        next2.click()
