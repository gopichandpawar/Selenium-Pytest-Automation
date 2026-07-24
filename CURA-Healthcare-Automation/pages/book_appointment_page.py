from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class MakeAppointment:
    def __init__(self,driver):
        self.driver = driver

    def Appointment(self):
        facility = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//select[@id='combo_facility']"))
        )
        select = Select(facility)
        select.select_by_value("Hongkong CURA Healthcare Center")

        readmission = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='chk_hospotal_readmission']"))
        )
        self.driver.execute_script("arguments[0].click();",readmission)

        health_program = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='radio_program_medicaid']"))
        )
        self.driver.execute_script("arguments[0].click();", health_program)

        date = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='txt_visit_date']"))
        )
        date.send_keys("22/07/2026")

        comment = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='txt_comment']"))
        )
        comment.send_keys("We can book the appointment using this application")

        appointment_book = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-book-appointment']"))
        )
        appointment_book.click()