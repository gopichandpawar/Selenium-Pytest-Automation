from pages.customer_page import Customers

def test_customer(driver):
    try:
        cust = Customers(driver)
        cust.bank_management()
        cust.customer()
        cust.search_customer("Harry")
        cust.delete_customer()

    except Exception as e:
        driver.save_screenshot("screenshort/test_fail.png")
        print(f"Test failed: {e}")
        raise  # Re-raises the exception so the test is marked as failed