from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.vehicle_locators import VehicleLocators
from selenium.webdriver.support.ui import Select

class VehiclePage:
    def __init__(self,driver):
        self.driver = driver

    def Vehicle_Data(self,veh_data):
        automobile = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,VehicleLocators.AUTOMOBILE))
        )
        automobile.click()

        # ------------------------------enter vehicle data----------------------

        make = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.MAKE))
        )
        select = Select(make)
        select.select_by_value(veh_data['make1'])

        engine_p = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.ENGINEER_PERFORMANCE))
        )
        engine_p.send_keys(veh_data['engine_p1'])

        date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,VehicleLocators.DATE))
        )
        date.send_keys(veh_data['date1'])

        num_of_seat = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.NUM_OF_SEAT))
        )
        select = Select(num_of_seat)
        select.select_by_value(veh_data['num_of_seat1'])

        fuel_type = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,VehicleLocators.FUEL_TYPE))
        )
        select = Select(fuel_type)
        select.select_by_value(veh_data['fuel_type1'])

        list_price = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.LIST_PRICE))
        )
        list_price.send_keys(veh_data['list_price1'])

        license_plat_num = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.LICENSE_PLATE_NUMBER))
        )
        license_plat_num.send_keys(veh_data['license_plat_num1'])

        annual_mileage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.ANNUAL_MILEAGE))
        )
        annual_mileage.send_keys(veh_data['annual_mileage1'])

        next = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VehicleLocators.NEXT))
        )
        next.click()