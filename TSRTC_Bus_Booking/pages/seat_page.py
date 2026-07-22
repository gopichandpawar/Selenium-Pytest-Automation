from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeatPage:
    def __init__(self,driver):
        self.driver = driver

    def Seat_selection(self):
        # ___________________________View Bus____________________________
        view_bus = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[@type='button'])[4]"))
        )
        view_bus.click()

        # ____________________________Select your Boarding/Dropping Point ___________________________
        boarding = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='boardingPoint']"))
        )
        boarding.click()

        pick_up_booking = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='ADONI BS - 20:30 ']"))
        )
        pick_up_booking.click()

        dropping = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='droppingPoint']"))
        )
        dropping.click()

        pick_up_dropping = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='SHAMSHABAD - 02:15']"))
        )
        pick_up_dropping.click()

        submit = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='submit'])[2]"))
        )
        submit.click()

        #window handling

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

        # ____________________________ Seat Select ___________________________
        seat = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='available_seat']//label)[10]"))
        )
        seat.click()

        select = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[@type='button'])[4]"))
        )
        select.click()

        submit = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[@type='submit'])[2]"))
        )
        submit.click()

        select1 = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//button[@type='button'])[5]"))
        )
        select1.click()

