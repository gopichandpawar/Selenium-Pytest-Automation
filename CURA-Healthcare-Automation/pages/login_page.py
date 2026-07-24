from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def Make_Appointment(self):
        appointment = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@href='./profile.php#login']"))
        )
        appointment.click()

    def Login(self,username,password):
        username1 = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//input[@name='username']"))
        )
        username1.send_keys(username)

        password1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password1.send_keys(password)

        submit = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-login']"))
        )
        submit.click()