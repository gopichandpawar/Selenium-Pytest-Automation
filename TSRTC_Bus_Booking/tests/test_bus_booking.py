from pages.search_page import SearchPage
from pages.seat_page import SeatPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage

def test_bus_booking_page(driver):

    try:
        search = SearchPage(driver)
        search.search_bus("ADONI","HYDERABAD")

        seat = SeatPage(driver)
        seat.Seat_selection()

        passenger = PassengerPage(driver)
        passenger.passenger_details()

        payment = PaymentPage(driver)
        payment.Payment_Details()

    except Exception as e:
        print(driver.save_screenshot("screenshots/abc.png"))
        print(f"Test Failed..! {e}")