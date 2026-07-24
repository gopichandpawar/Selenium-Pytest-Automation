from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Menu_Google:
    def __init__(self,driver):
        self.driver = driver

    def Menu(self):
        m_google = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@id='menu-toggle']"))
        )
        m_google.click()

        history = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@href='history.php#history']"))
        )
        history.click()

