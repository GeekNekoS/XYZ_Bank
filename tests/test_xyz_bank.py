from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from XyzPages import SearchTools
from datetime import date
import datetime
import logging
import allure
import time
import csv


@allure.severity("Blocker")
def test_xyz_bank_new_version(setup_method):
    LOGGER = logging.getLogger(__name__)

    # №2
    driver = SearchTools(setup_method)
    driver.go_to_site()
    LOGGER.info("1/8] Openning the page")

    # №3
    driver.click_the_button("//button[text()='Customer Login']")
    #
    username_button = driver.click_the_button("//select[@name='userSelect']/option[text()='Harry Potter']")
    assert username_button.text == "Harry Potter"
    LOGGER.info("2/8] User selection attempt")
    #
    driver.click_the_button("//button[text()='Login']")

    # №4 fib_money
    n = date.today().day
    fib = lambda x: 1 if x < 3 else fib(x - 2) + fib(x - 1)
    money = fib(n)
    LOGGER.info("3/8] The N fibonacci number calculation")

    count_transactions = 0

    # №5 deposit
    driver.click_the_button("//button[@ng-click='deposit()']")
    #
    driver.write_input("//input[@placeholder='amount']", money)
    #
    driver.click_the_button("//button[text()='Deposit']")
    #
    count_transactions += 1
    LOGGER.info("4/8] Adding funds to account")

    # №6 withdrawal
    driver.click_the_button("//button[@ng-click='withdrawl()']")
    time.sleep(1)  #
    #
    driver.write_input("//input[@placeholder='amount']", money)
    #
    driver.click_the_button("//button[text()='Withdraw']")
    time.sleep(1)  #
    #
    count_transactions += 1
    LOGGER.info("5/8] Debiting from the account")

    # №7
    balance_info = driver.check_info_of_element("//div[@ng-hide='noAccount']/strong[2]")
    assert balance_info.text == "0"
    LOGGER.info("6/8] Сhecking the account balance")

    # №8 <== где-то здесь ошибка
    driver.click_the_button("//button[@ng-click='transactions()']")
    #
    transactions = driver.check_info_of_elements("//table/tbody/tr")
    assert len(transactions) == count_transactions
    LOGGER.info("7/8] Checking the number of taranactions")

    # №9
    with open(f'transactions_check.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',')

        headers = ["Date-Time", " Amount", "Transaction Type"]
        writer.writerow(headers)

        for transaction in transactions:

            transaction_info = transaction.find_elements(By.XPATH, ".//td")
            #
            date_time_str, amount, transaction_type = transaction_info
            date_time = datetime.datetime.strptime(date_time_str.text, "%b %d, %Y %H:%M:%S %p")
            info = [date_time.strftime('%d %B %Y %H:%M:%S'), amount.text, transaction_type.text]
            writer.writerow(info)
    LOGGER.info("8/8]" + f"\033[38;5;{231}m {'Generating a report file'}\033[0;0m")


@allure.severity("Blocker")
def test_xyz_bank_old_version(setup_method):
    LOGGER = logging.getLogger(__name__)
    # №2
    driver = setup_method
    driver.get(url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    time.sleep(1)
    with allure.step("Скриншот открываемой страницы XYZ_Bank"):
        allure.attach(driver.get_screenshot_as_png(), name="main_page", attachment_type=AttachmentType.PNG)
    assert driver.title == "XYZ Bank"
    LOGGER.info("1/8]" + f"\033[38;5;{231}m {'Openning the page'}\033[0;0m")

    # №3
    customer_login_button = driver.find_element(By.XPATH, "//button[text()='Customer Login']")
    customer_login_button.click()
    time.sleep(1)
    #
    username_button_xpath = "//select[@name='userSelect']/option[text()='Harry Potter']"
    username_button = driver.find_element(By.XPATH, username_button_xpath)
    assert username_button.text == "Harry Potter"
    LOGGER.info("2/8]" + f"\033[38;5;{231}m {'User selection attempt'}\033[0;0m")
    username_button.click()
    time.sleep(1)
    #
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()
    time.sleep(1)

    # №4 fib_money
    n = date.today().day
    fib = lambda x: 1 if x < 3 else fib(x - 2) + fib(x - 1)
    money = fib(n)
    LOGGER.info("3/8]" + f"\033[38;5;{231}m {'The N fibonacci number calculation'}\033[0;0m")

    count_transactions = 0

    # №5 deposit
    deposit_button = driver.find_element(By.XPATH, "//button[@ng-click='deposit()']")
    deposit_button.click()
    time.sleep(1)
    #
    amount_input = driver.find_element(By.XPATH, "//input[@placeholder='amount']")
    amount_input.send_keys(money)
    time.sleep(1)
    #
    send_deposit = driver.find_element(By.XPATH, "//button[text()='Deposit']")
    send_deposit.click()
    time.sleep(1)
    #
    count_transactions += 1
    LOGGER.info("4/8]" + f"\033[38;5;{231}m {'Adding funds to account'}\033[0;0m")

    # №6 withdrawal
    withdrawal_button = driver.find_element(By.XPATH, "//button[@ng-click='withdrawl()']")
    withdrawal_button.click()
    time.sleep(1)
    #
    amount_input = driver.find_element(By.XPATH, "//input[@placeholder='amount']")
    amount_input.send_keys(money)
    time.sleep(1)
    #
    send_withdrawal = driver.find_element(By.XPATH, "//button[text()='Withdraw']")
    send_withdrawal.click()
    time.sleep(1)
    #
    count_transactions += 1
    LOGGER.info("5/8]" + f"\033[38;5;{231}m {'Debiting from the account'}\033[0;0m")

    # №7
    balance_info = driver.find_element(By.XPATH, "//div[@ng-hide='noAccount']/strong[2]")
    assert balance_info.text == "0"
    LOGGER.info("6/8]" + f"\033[38;5;{231}m {'Сhecking the account balance'}\033[0;0m")
    time.sleep(1)

    # №8
    withdrawal_button = driver.find_element(By.XPATH, "//button[@ng-click='transactions()']")
    withdrawal_button.click()
    time.sleep(1)
    #
    transactions = driver.find_elements(By.XPATH, "//table/tbody/tr")
    assert len(transactions) == count_transactions
    LOGGER.info("7/8]" + f"\033[38;5;{231}m {'Checking the number of taranactions'}\033[0;0m")

    # №9
    with open(f'transactions.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',')

        headers = ["Date-Time", " Amount", "Transaction Type"]
        writer.writerow(headers)

        for transaction in transactions:
            transaction_info = transaction.find_elements(By.XPATH, ".//td")
            date_time_str, amount, transaction_type = transaction_info
            date_time = datetime.datetime.strptime(date_time_str.text, "%b %d, %Y %H:%M:%S %p")
            info = [date_time.strftime('%d %B %Y %H:%M:%S'), amount.text, transaction_type.text]
            writer.writerow(info)
    with allure.step("Скриншот таблицы, двух проведённых транзакций"):
        allure.attach(driver.get_screenshot_as_png(), name="main_page", attachment_type=AttachmentType.PNG)
    LOGGER.info("8/8]" + f"\033[38;5;{231}m {'Generating a report file'}\033[0;0m")
