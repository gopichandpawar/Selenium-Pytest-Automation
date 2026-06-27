from pages.add_customer_page import AddCustomer

def test_add_customer(driver):

    try:
        add_c = AddCustomer(driver)
        add_c.bank_management()
        add_c.bank_management()
        add_c.add_customer("Gopichand", "Pawar", 997898)

    except Exception as e:
        driver.save_screenshot("screenshort/test_fails.png")
        print(f"Test failed: {e}")