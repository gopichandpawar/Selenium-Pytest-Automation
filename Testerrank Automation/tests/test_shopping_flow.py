from pages.practice_page import PracticePage
from pages.product_page import ProductPage
from pages.address_page import AddressPage
from pages.payment_page import PaymentPage
from test_data.test_data1 import CARD
from test_data.test_data1 import CUSTOMER

def test_shopping_flow(driver):
    try:
        prac = PracticePage(driver)
        prac.Pactice_Page()

        prod = ProductPage(driver)
        prod.click_product()
        prod.select_quantity()
        prod.click_the_buy_now()
        prod.click_place_order()

        add = AddressPage(driver)
        add.address_detail(CUSTOMER)

        payment = PaymentPage(driver)
        payment.payment_details(CARD)

    except Exception as e:
        print(driver.save_screenshot("screenshorts/abc.png"))
        print(f"script failed {e}..!")
