from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self,driver):
        self.driver = driver

    def search_bus(self,from_city,to_city):

        try:
            popup = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='close_icon']"))
            )
            popup.click()  # <-- Missing in your code

            # Wait for overlay to disappear
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located((By.ID, "faded"))
            )

        except Exception as e:
            print(f"Popup handling failed: {e}")

        # ___________________________From Input____________________________

        from_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ant-select-selection-search-input"))
        )
        from_input.click()
        from_input.send_keys(from_city)

        pick_from_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='ADONI']"))
        )
        pick_from_input.click()

        # ___________________________To Input____________________________
        inputs = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "input.ant-select-selection-search-input")
            )
        )

        to_input = inputs[1]  # Second input = Destination
        to_input.click()
        to_input.send_keys(to_city)

        pick_to_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='HYDERABAD']"))
        )
        pick_to_input.click()

        # ___________________________Date____________________________
        date = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Today']"))
        )
        date.click()

        # ___________________________Search Bus____________________________
        search = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search.click()
