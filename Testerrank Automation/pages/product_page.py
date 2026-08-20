from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.product_locators import ProductLocators
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self,driver):
        self.driver = driver

    def click_product(self):
        product = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,ProductLocators.PRODUCT))
        )
        print(f"text: {product.text}")
        print(f"link: {product.get_attribute('href')}")
        product.click()

    def select_quantity(self):
        quantity = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,ProductLocators.QUANTITY))
        )
        select = Select(quantity)
        select.select_by_value("2")

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def click_the_buy_now(self):
        buy = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,ProductLocators.BUY))
        )
        buy.click()

    def click_place_order(self):
        place_order = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,ProductLocators.PLACE_ORDER))
        )
        place_order.click()