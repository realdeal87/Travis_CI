"""Модуль для удаленного запуска тестов"""
import pytest
from selenium import webdriver


@pytest.fixture
def browser_stack(request):
    """Фикстура для запуска тестов в облачном сервисе BrowserStack"""
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '77.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1280x1024',
        'name': 'Bstack-[Python] Sample Test'
    }

    driver = webdriver.Remote(
        command_executor='https://realdeal1:4ANpga6WpDDuecaiUfhw@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
    request.addfinalizer(driver.quit)
    return driver


def test_test1(browser_stack):
    pass


def test_test2(browser_stack):
    pass


def test_test3(browser_stack):
    pass
