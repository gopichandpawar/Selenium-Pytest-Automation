# Testerrank Practice Page Automation

## 📌 Project Overview

This project is a UI automation testing framework developed using Python, Selenium WebDriver, and Pytest.

The automation is performed on the Testerrank practice page:

https://www.testerrank.com/practice

The framework follows the Page Object Model (POM) design pattern.

The framework separates:

- Test cases
- Page actions
- Locators
- Test data
- Configuration

This makes the framework easier to maintain and reuse.

---

## 🛠️ Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git/GitHub

---

## 📁 Project Structure

```text
project/
│
├── pages/
│   ├── practice_page.py
│   ├── product_page.py
│   ├── address_page.py
│   └── payment_page.py
│
├── locators/
│   ├── practice_locators.py
│   ├── product_locators.py
│   ├── address_locators.py
│   └── payment_locators.py
│
├── test_data/
│   └── test_data1.py
│
├── tests/
│   └── test_shopping_flow.py
│
├── screenshots/
│
├── conftest.py
├── requirements.txt
└── README.md
