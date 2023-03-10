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
    time.sleep(1)
    with allure.step("Скриншот открываемой страницы XYZ_Bank"):
        allure.attach(driver.get_screenshot_as_png(), name="main_page", attachment_type=AttachmentType.PNG)
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

    #
    driver.click_the_button("//button[@ng-click='transactions()']")
    #
    transactions = driver.check_info_of_elements("//table/tbody/tr")
    assert len(transactions) == count_transactions
    LOGGER.info("7/8] Checking the number of taranactions")

    # №9
    with open(f'transactions_test_1.csv', 'w', encoding="utf-8", newline='') as file:
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
    with allure.step("Скриншот страницы проведённых транзакций"):
        allure.attach(driver.get_screenshot_as_png(), name="main_page", attachment_type=AttachmentType.PNG)
    LOGGER.info("8/8] Generating a report file")
