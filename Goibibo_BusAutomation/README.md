# Bus Ticket Booking Automation

## Project Overview

This project automates the major functionalities of a Bus Ticket Booking web application using Selenium WebDriver with Python and PyTest.

The framework follows the Page Object Model (POM) design pattern to improve code reusability, maintainability, and scalability.

## Modules Covered

* Bus Search
* Select Bus
* Seat Selection
* Passenger Details
* Payment
* Booking Confirmation
* My Trips
* Ticket Cancellation

## Technology Stack

* Python
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* HTML Test Reports
* Git
* GitHub

## Project Structure

```text
Bus_Ticket_Booking_Automation/
│
├── tests/
│   ├── test_bus_search.py
│   ├── test_select_bus.py
│   ├── test_seat_selection.py
│   ├── test_passenger.py
│   └── test_payment.py
│
├── pages/
│   ├── bus_search_page.py
│   ├── select_bus_page.py
│   ├── seat_selection_page.py
│   ├── passenger_page.py
│   └── payment_page.py
│
├── test_data.py/
│  
├── config/
│   └── config.ini
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
│

```

## Test Scenarios

### 1. Bus Search

* Verify source location can be selected.
* Verify destination location can be selected.
* Verify travel date can be selected.
* Verify buses are displayed for valid search criteria.
* Verify appropriate validation for invalid search criteria.

### 2. Select Bus

* Verify available buses are displayed.
* Verify user can select a bus.
* Verify bus details are displayed correctly.
* Verify boarding and dropping points.

### 3. Seat Selection

* Verify available seats are displayed.
* Verify user can select an available seat.
* Verify selected seat is highlighted.
* Verify already booked seats cannot be selected.
* Verify seat price is displayed correctly.

### 4. Passenger Details

* Verify passenger name can be entered.
* Verify age can be entered.
* Verify gender can be selected.
* Verify mobile number validation.
* Verify mandatory field validations.

### 5. Payment

* Verify payment page is displayed.
* Verify booking amount is displayed correctly.
* Verify payment details can be entered.
* Verify successful payment.
* Verify payment failure scenario.
* Verify booking confirmation after successful payment.

## Framework Features

* Page Object Model
* Reusable page classes
* PyTest fixtures
* Explicit waits
* Configuration management
* Test data management
* Screenshot capture on failure
* HTML test reports
* Exception handling
* Cross-browser execution support

## Locators Used

The automation framework uses different Selenium locators depending on the application:

* ID
* Name
* Class Name
* CSS Selector
* XPath
* Link Text
* Partial Link Text

Dynamic XPath techniques such as `contains()` and `starts-with()` are used where required.

## How to Install

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Execute Tests

Run all tests:

```bash
pytest
```

Run a specific module:

```bash
pytest tests/test_bus_search.py
```

Run with HTML report:

```bash
pytest --html=reports/test_report.html
```

## Reporting

After execution, an HTML test report is generated inside the `reports` folder.

The report contains:

* Total tests
* Passed tests
* Failed tests
* Execution time
* Test details

## Future Enhancements

* Add API testing using Postman/REST Assured
* Add database validation using SQL
* Integrate with Jenkins CI/CD
* Add cross-browser testing using Selenium Grid
* Add parallel test execution
* Integrate Allure reporting

## Author

Gopichand Pawar

QA Automation Engineer | Python | Selenium | PyTest | API Testing | SQL
