# Insurance Automation Python

## Project Overview

Insurance Automation Python is a Selenium WebDriver automation framework developed using Python, PyTest and Page Object Model (POM).

The framework automates an insurance application flow including vehicle details, insurance details, product selection and quote generation.

## Technologies Used

* Python
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* PyTest HTML Report
* Git and GitHub

## Application Flow

1. Open Insurance Application
2. Enter Vehicle Details
3. Enter Insurance Details
4. Select Insurance Product
5. Generate Quote
6. Validate Quote Details
7. End-to-End Flow Validation

## Project Structure

```text
Insurance_Automation_Python/
│
├── tests/
├── pages/
├── locators/
├── utils/
├── test_data/
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Framework Design

The framework follows the Page Object Model design pattern.

```text
Test Cases
    ↓
Page Classes
    ↓
Locator Classes
    ↓
Web Application
```

## Test Cases

The framework covers:

* Valid vehicle details
* Invalid vehicle details
* Mandatory field validation
* Insurance details validation
* Product selection
* Quote generation
* Quote validation
* End-to-end insurance flow

## Installation

Clone the project and navigate to the project directory.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Execution

Run all test cases:

```bash
pytest
```

Run tests in verbose mode:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_vehicle_details.py -v
```

## Reports

After execution, the PyTest HTML report is generated in:

```text
reports/report.html
```

## Screenshots

Screenshots can be captured during test execution, especially when a test fails.

They are stored inside:

```text
screenshots/
```

## Key Framework Features

* Page Object Model
* Separate locator classes
* Reusable PyTest fixtures
* Explicit waits
* Test data separation
* HTML reporting
* Screenshot capture
* Modular and maintainable test scripts
* Positive and negative test scenarios

## Author

Gopichand Pawar
