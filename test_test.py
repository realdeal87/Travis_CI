import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    """Фикстура запускает браузеры, установленные в параметрах, и
    открывает страницу """
    browser = request.param
    if browser == "Chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        web = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        web = webdriver.Firefox(options=options)
    else:
        raise Exception("is not supported!")
    web.maximize_window()
    web.get("https://debian.org")
    request.addfinalizer(web.quit)
    return web


def test_test1(driver):
    pass


def test_test2(driver):
    pass


def test_test3(driver):
    pass
