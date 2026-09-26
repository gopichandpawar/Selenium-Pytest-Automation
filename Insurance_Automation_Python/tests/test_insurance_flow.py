from pages.vehicle_page import VehiclePage
from pages.insurance_page import InsurancePage
from pages.product_page import ProductPage
from pages.send_quote_page import SendQuotePage
from pages.price_option_page import PriceOptionPage
from test_data.test_data1 import VEHICLE
from test_data.test_data1 import INSURANCE
from test_data.test_data1 import PRODUCT
from test_data.test_data1 import SEND_QUOTE

def test_insurance_flow(driver):
    try:
        vehicle = VehiclePage(driver)
        vehicle.Vehicle_Data(VEHICLE)

        insurance = InsurancePage(driver)
        insurance.Insurance_Data(INSURANCE)

        product = ProductPage(driver)
        product.Product_Data(PRODUCT)

        price = PriceOptionPage(driver)
        price.Price_Option_Data()

        send_quote = SendQuotePage(driver)
        send_quote.Send_Quote_data(SEND_QUOTE)

    except Exception as e:
        driver.save_screenshot("screenshots/abc.png")
        print(f"script failed {e}")
