# Banking Application Test Automation Framework

## Overview

This project is a UI test automation framework developed using **Python**, **Selenium WebDriver**, and **Pytest**. It automates key functionalities of the GlobalSQA Banking Application by following the **Page Object Model (POM)** design pattern.

## Application Under Test

* GlobalSQA Banking Application
* URL: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* HTML Reports

## Project Structure

```text
├── pages/
├── tests/
├── utilities/
├── Reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Scenarios Automated

* Login
* Add Customer
* Open Account
* Customer Management
* Account Management

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Execute Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Generate an HTML report:

```bash
pytest --html=Reports/report.html --self-contained-html
```

## Sample Test Result

```text
tests/test_account_manage.py::test_login_page PASSED
tests/test_add_customer1.py::test_add_customer PASSED
tests/test_customer1.py::test_customer PASSED
tests/test_login.py::test_login_page PASSED
tests/test_open_account1.py::test_add_customer PASSED

================== 5 passed ==================
```

## Reports

After test execution, an HTML report is generated in the `Reports/` directory. The report provides:

* Total number of test cases executed
* Passed and failed test summary
* Execution duration
* Detailed results for each test case

## Future Enhancements

* Cross-browser testing
* Parallel execution with pytest-xdist
* Jenkins CI/CD integration
* Screenshot capture for failed tests
* Logging support
