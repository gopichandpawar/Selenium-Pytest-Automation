from pages.history_page import Menu_Google
from pages.login_page import LoginPage

def test_menu_google(driver):
    try:
        login = LoginPage(driver)
        login.Make_Appointment()
        login.Login("John Doe", "ThisIsNotAPassword")

        menu1 = Menu_Google(driver)
        menu1.Menu()

    except Exception as e:
        print(driver.save_screenshot("reports/screenshots/abc.png"))
        print(f"script failed {e}..!")