import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class CreateRoutePage(BasePage):
    START_ROUTE = (
        By.XPATH, ".//label[text()='Откуда']/preceding-sibling::input"
    )
    END_ROUTE = (
        By.XPATH, ".//label[text()='Куда']/preceding-sibling::input"
    )
    POINT_ROUTE_WITH_ADDRESS = lambda address: (
        By.XPATH, f".//div[@id='map']//*[text()='{address}']"
    )

    @allure.step("Set up a start route with {address}")
    def set_start_route(self, address):
        self.input(CreateRoutePage.START_ROUTE, address)

    @allure.step("Set up an end route with {address}")
    def set_end_route(self, address):
        self.input(CreateRoutePage.END_ROUTE, address)

    @allure.step("A point route is available with {address}")
    def is_address_available(self, address):
        self.wait_visibility_of_element_located(
            CreateRoutePage.POINT_ROUTE_WITH_ADDRESS(address)
        )
        return True
        