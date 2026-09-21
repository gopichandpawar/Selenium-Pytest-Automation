from pages.bus_search_page import BusSearchPage
from pages.bus_selection_page import BusSelectPage
from pages.seat_selection_page import SeatSelectPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage
from test_data.test_data1 import PASSENGER

def test_booking_flow(driver):
    try:

        bus = BusSearchPage(driver)
        bus.Bus_Search("Pune", "Yavatmal")

        bus_select = BusSelectPage(driver)
        bus_select.Bus_Select()

        seat_select = SeatSelectPage(driver)
        seat_select.Seat_Select()

        passenger1 = PassengerPage(driver)
        passenger1.Passenger_Details(PASSENGER)

        payment = PaymentPage(driver)
        payment.Payment_Details()

    except Exception as e:
        driver.save_screenshot("reports/abc.png")
        print(f"script failed: {e}")

