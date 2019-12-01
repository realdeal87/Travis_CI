"""Модуль для удаленного запуска тестов"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


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


def test_open_page(browser_stack):
    """Открытие страницы otus.ru и клик на логотипе"""
    browser_stack.get("https://otus.ru")
    if "OTUS - Онлайн-образование" not in browser_stack.title:
        raise Exception("Unable to load google page!")
    elem = browser_stack.find_element_by_class_name("header2__logo-img")
    elem.click()


def test_drag_n_drop(browser_stack):
    """Добавление документов в корзину"""
    browser_stack.get("https://marcojakob.github.io/dart-dnd/basic/")
    documents = browser_stack.find_elements_by_class_name("document")
    trash = browser_stack.find_element_by_class_name("trash")
    for document in documents:
        ActionChains(browser_stack).drag_and_drop(document, trash).perform()


def test_add_to_wishlist(browser_stack):
    """Добавление iPhone в список желаемых товаров"""
    browser_stack.get("https://demo.opencart.com/")
    like_buttons = browser_stack.find_elements_by_xpath(
        "//button[@data-original-title='Add to Wish List']")
    like_buttons[1].click()
