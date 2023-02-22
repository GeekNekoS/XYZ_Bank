from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture
def setup_method():
    options = Options()
    # options.add_argument('start-maximized')  # запуск тестов на полный экран
    # options.add_argument('--headless')  # запуск тестов без UI интерфейса

    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    yield driver
    driver.quit()
