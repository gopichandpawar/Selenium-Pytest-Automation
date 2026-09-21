from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.seat_selectoin_locator import SeatSelectLocator

class SeatSelectPage:
    def __init__(self, driver):
        self.driver = driver

    def Seat_Select(self):
        seat_select = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,SeatSelectLocator.SEAT_SELECT))
        )
        seat_select.click()

        boarding = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SeatSelectLocator.BOARDING_POINT))
        )
        self.driver.execute_script("arguments[0].click();", boarding)

        continue2 = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, SeatSelectLocator.CONTINUE2))
        )
        continue2.click()

# ___________________________window handle_________________________
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
