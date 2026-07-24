from pages.book_appointment_page import MakeAppointment
from pages.login_page import LoginPage

def test_book_appointment_page(driver):

    try:
        login = LoginPage(driver)
        login.Make_Appointment()
        login.Login("John Doe","ThisIsNotAPassword")

        book = MakeAppointment(driver)
        book.Appointment()

    except Exception as e:
        print(driver.save_screenshot("reports/screenshots/abc.png"))
        print(f"script failed {e}..!")