from pages.login_page import LoginPage

def test_login_page(driver):

    try:
        login = LoginPage(driver)
        login.login_page()
        login.select_dropdown()
        login.login_button()

    except Exception as e:
        driver.save_screenshot("screenshort/test_fail.png")
        print(f"Test failed: {e}")