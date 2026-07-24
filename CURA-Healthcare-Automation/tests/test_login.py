from pages.login_page import LoginPage

def test_login_page(driver):

    try:
        login = LoginPage(driver)
        login.Make_Appointment()
        login.Login("John Doe","ThisIsNotAPassword")

    except Exception as e:
        print(driver.save_screenshot("reports/screenshots/abc.png"))
        print(f"script failed {e}..!")

