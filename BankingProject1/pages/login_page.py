from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def login_page(self):
        customer_login = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[text()='Customer Login']"))
        )
        customer_login.click()

    def select_dropdown(self):
        dropdown = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@id='userSelect']"))
        )
        select = Select(dropdown)
        select.select_by_visible_text("Harry Potter")

    def login_button(self):
        login = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))
        )
        login.click()


