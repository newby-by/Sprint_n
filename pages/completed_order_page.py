import re

import allure
from selenium.webdriver.common.by import By

import data
from .wait_page import WaitPage


class ComplitedOrderPage(WaitPage):

    CAR_NUMBER = (
        By.XPATH, ".//div[@class='number']"
    )
    IMAGE_TARIFF = (
        By.XPATH, ".//div[@class='order-number']/img"
    )
    RATING = (
        By.XPATH, ".//div[@class='order-btn-rating']"
    )
    DRIVER_NAME = (
        By.XPATH,
        ".//div[@class='order-btn-rating']/parent::div/following-sibling::div"
    )
    FOTO_DRIVER = (
        By.XPATH,
        ".//div[@class='order-btn-rating']/following-sibling::img"
    )

    @allure.step("The complited order page is closed")
    def is_not_visible(self):
        self.wait_element_became_invisibile(ComplitedOrderPage.CAR_NUMBER)
        return True

    @allure.step("The complited order page has car number")
    def has_car_number(self):
        car_number = self.get_text(ComplitedOrderPage.CAR_NUMBER)
        return bool(
            re.fullmatch(data.ComplitedOrderData.CAR_NUMBER_PATTERN,
                         car_number)
        )

    @allure.step("The complited order page has raiting")
    def has_raiting(self):
        raiting: str = self.get_text(ComplitedOrderPage.RATING)
        return isinstance(float(raiting.replace(",", ".")), float)

    @allure.step("The complited order page has driver name")
    def has_car_driver_name(self):
        driver_name = self.get_text(ComplitedOrderPage.DRIVER_NAME)
        return bool(
            re.fullmatch(data.ComplitedOrderData.CAR_DRIVER_NAME_PATTERN,
                         driver_name)
        )

    @allure.step("The complited order page has tariff image")
    def has_image_tariff(self):
        self.wait_visibility_of_element_located(
            ComplitedOrderPage.IMAGE_TARIFF
        )
        return True

    @allure.step("The complited order page has foto driver")
    def has_foto_driver(self):
        self.wait_visibility_of_element_located(
            ComplitedOrderPage.FOTO_DRIVER
        )
        return True

    @allure.step("Waiting show up the complited order page")
    def wait_show_up_complited_order_page(self):
        self.wait_text_to_be_present_in_element(
            ComplitedOrderPage.TITLE,
            _text=data.ComplitedOrderData.TITLE,
            time=data.ComplitedOrderData.TIME_FOR_WAITING
        )
