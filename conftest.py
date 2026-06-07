import base64
import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import data
import pages


# Monkey Patch the base64 Module
if not hasattr(base64, 'encodestring'):
    base64.encodestring = base64.encodebytes


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help=("The key to choose a browser: chrome or firefox. "
              "By default: chrome."),
        choices=("chrome", "firefox", "remote")
    )


@pytest.fixture(scope='function')
def driver(pytestconfig):
    if pytestconfig.getoption("browser") == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif pytestconfig.getoption("browser") == "firefox":
        os.environ['GH_TOKEN'] = os.getenv('GH_TOKEN')
        try:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        except SessionNotCreatedException:
            # if the path to firefox binary file is not found
            load_dotenv()
            options = Options()
            options.binary_location = os.getenv('BINARY_LOCATION_FIREFOX')
            driver = webdriver.Firefox(
                options=options,
                executable_path=GeckoDriverManager().install()
            )
    elif pytestconfig.getoption("browser") == "remote":
        options = ChromeOptions()
        options.set_capability('acceptInsecureCerts', True)
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            desired_capabilities=capabilities,
            options=options)
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def route_with_different_addresses(driver):
    create_route = pages.CreateRoutePage(driver)
    create_route.open(data.BASE_URL)
    create_route.set_start_route(data.ADDRESSES[0])
    create_route.set_end_route(data.ADDRESSES[1])

    return create_route.driver


@pytest.fixture(scope='function')
def route_with_the_same_addresses(driver):
    create_route = pages.CreateRoutePage(driver)
    create_route.open(data.BASE_URL)
    create_route.set_start_route(data.ADDRESSES[0])
    create_route.set_end_route(data.ADDRESSES[0])

    return create_route.driver


@pytest.fixture(scope='function')
def order_taxi_form(route_with_different_addresses):
    chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
    chose_route_page.choose_rapid_route()
    chose_route_page.click_on_button_order_taxi()

    order_taxi = pages.OrderTaxiForm(chose_route_page.driver)
    return order_taxi.driver


@pytest.fixture(scope='function')
def ordered_taxi(order_taxi_form):
    order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
    order_taxi_page.choose_tariff("Рабочий")
    order_taxi_page.order_with_requirement_table()

    return order_taxi_page.driver
