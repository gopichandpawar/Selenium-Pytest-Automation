from pages.open_account_page import OpenAccount

def test_add_customer(driver):

    try:
        open_a = OpenAccount(driver)
        open_a.bank_management()
        open_a.open_account()

    except Exception as e:
        driver.save_screenshot("screenshort/test_fail.png")
        print(f"Test failed: {e}")