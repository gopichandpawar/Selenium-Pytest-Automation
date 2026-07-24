# CURA Healthcare Automation Framework

## Project Overview

This project is developed using Selenium with Python, Pytest, and the Page Object Model (POM) design pattern to automate the CURA Healthcare demo application.

## Technology Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- WebDriver Manager
- Pytest HTML Report

## Project Structure

```
CURA-Healthcare-Automation/
│
├── pages/
├── tests/
├── reports/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Application URL

https://katalon-demo-cura.herokuapp.com/

## Test Modules

- Login
- Make Appointment
- Appointment History
- Logout

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd CURA-Healthcare-Automation
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Run All Tests

```bash
pytest
```

## Run Smoke Tests

```bash
pytest -m smoke
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

## Features

- Selenium WebDriver
- Pytest Framework
- Page Object Model (POM)
- Explicit Waits
- HTML Reports
- Cross-browser ready
- Reusable Page Classes

## Author

Your Name