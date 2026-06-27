from pages.login_page import LoginPage
from pages.deposit_page import DepositPage
from pages.withdrawl_page import WithdrawlPage
from pages.Transactions_page import TransactionsPage

def test_login_page(driver):

    try:
        login = LoginPage(driver)
        login.login_page()
        login.select_dropdown()
        login.login_button()

        depo = DepositPage(driver)
        depo.Deposit(2000)

        with_d = WithdrawlPage(driver)
        with_d.Withdrawl(500)

        tran = TransactionsPage(driver)
        tran.transaction_page()

    except Exception as e:
        driver.save_screenshot("screenshort/test_fails.png")
        print(f"Test failed: {e}")

