import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ChooseRoutePage(BasePage):

    TYPE_BLOCK = (
        By.XPATH, ".//div[contains(@class,'type-picker')]"
    )
    OPTIMAL_ROUTE = (
        By.XPATH, ".//div[text()='Оптимальный']"
    )
    PRICE_INFO_ROUTE = (
        By.XPATH, "(.//div[@class='results-text']/div)[1]"
    )
    DURING_INFO_ROUTE = (
        By.XPATH, "(.//div[@class='results-text']/div)[2]"
    )
    RAPID_ROUTE = (
        By.XPATH, ".//div[text()='Быстрый']"
    )
    MYSELF_ROUTE = (
        By.XPATH, ".//div[text()='Свой']"
    )
    ORDER_TAXI_BUTTON = (By.XPATH, ".//button[text()='Вызвать такси']")
    BOOK_TAXI_BUTTON = (By.XPATH, ".//button[text()='Забронировать']")
    TYPE_MOVEMENT = lambda id: (
        By.XPATH, f"(.//div[@class='types-container']/div)[{id}]"
    )

    @allure.step("The type block is available")
    def is_type_block_available(self):
        self.wait_visibility_of_element_located(ChooseRoutePage.OPTIMAL_ROUTE)
        self.wait_visibility_of_element_located(ChooseRoutePage.RAPID_ROUTE)
        self.wait_visibility_of_element_located(ChooseRoutePage.MYSELF_ROUTE)
        return 'shown' in self.get_attribute(ChooseRoutePage.TYPE_BLOCK,
                                             'class')

    @allure.step("The info block for the same addresses")
    def is_info_with_the_same_addresses_correct(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.PRICE_INFO_ROUTE
        )
        self.wait_visibility_of_element_located(
            ChooseRoutePage.DURING_INFO_ROUTE
        )

        return (
            self.get_text(
                ChooseRoutePage.PRICE_INFO_ROUTE
            ) == "Авто Бесплатно"
            and self.get_text(
                ChooseRoutePage.DURING_INFO_ROUTE
            ) == "В пути 0 мин."
        )

    @allure.step("The optimal route is active")
    def is_optimal_route_available(self):
        self.wait_visibility_of_element_located(ChooseRoutePage.OPTIMAL_ROUTE)
        self.wait_element_clickable(ChooseRoutePage.OPTIMAL_ROUTE)
        return "active" in self.get_attribute(
            ChooseRoutePage.OPTIMAL_ROUTE, 'class'
        )

    @allure.step("The rapid route is active")
    def is_rapid_route_available(self):
        self.wait_visibility_of_element_located(ChooseRoutePage.RAPID_ROUTE)
        self.wait_element_clickable(ChooseRoutePage.RAPID_ROUTE)
        return "active" in self.get_attribute(
            ChooseRoutePage.RAPID_ROUTE, 'class'
        )

    @allure.step("The myself route is active")
    def is_myself_route_available(self):
        self.wait_visibility_of_element_located(ChooseRoutePage.MYSELF_ROUTE)
        self.wait_element_clickable(ChooseRoutePage.MYSELF_ROUTE)
        return "active" in self.get_attribute(
            ChooseRoutePage.MYSELF_ROUTE, 'class'
        )

    @allure.step("The optimal route has a price and during of a trip")
    def is_info_about_optimal_route_correct(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.PRICE_INFO_ROUTE
        )
        self.wait_visibility_of_element_located(
            ChooseRoutePage.DURING_INFO_ROUTE
        )

        return (
            "Авто" in self.get_price_line_from_info_block()
            and "В пути" in self.get_during_line_from_info_block()
        )

    @allure.step("The rapid type has a price and "
                 "during of a trip and button 'Вызвать такси'")
    def is_info_about_rapid_route_correct(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.PRICE_INFO_ROUTE
        )
        self.wait_visibility_of_element_located(
            ChooseRoutePage.DURING_INFO_ROUTE
        )
        self.wait_visibility_of_element_located(
            ChooseRoutePage.ORDER_TAXI_BUTTON
        )
        self.wait_element_clickable(
            ChooseRoutePage.ORDER_TAXI_BUTTON
        )

        return (
            "Такси" in self.get_price_line_from_info_block()
            and "В пути" in self.get_during_line_from_info_block()
        )

    @allure.step("The myself type for 'Драйв' has a price and "
                 "during of a trip and button 'Забронировать'")
    def is_info_about_rapid_route_correct_with_carsharing(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.PRICE_INFO_ROUTE
        )
        self.wait_visibility_of_element_located(
            ChooseRoutePage.DURING_INFO_ROUTE
        )
        self.wait_visibility_of_element_located(
            ChooseRoutePage.BOOK_TAXI_BUTTON
        )
        self.wait_element_clickable(
            ChooseRoutePage.BOOK_TAXI_BUTTON
        )

        return (
            "Драйв" in self.get_price_line_from_info_block()
            and "В пути" in self.get_during_line_from_info_block()
        )

    @allure.step("Choose the optimal route")
    def choose_optimal_route(self):
        self.wait_element_clickable(ChooseRoutePage.OPTIMAL_ROUTE)
        self.click(ChooseRoutePage.OPTIMAL_ROUTE)

    @allure.step("Choose the rapid route")
    def choose_rapid_route(self):
        self.wait_element_clickable(ChooseRoutePage.OPTIMAL_ROUTE)
        self.click(ChooseRoutePage.RAPID_ROUTE)

    @allure.step("Choose the myself route")
    def choose_myself_route(self):
        self.wait_element_clickable(ChooseRoutePage.MYSELF_ROUTE)
        self.click(ChooseRoutePage.MYSELF_ROUTE)

    @allure.step("Choose a type with id = {id}")
    def choose_type_with(self, id):
        self.wait_element_clickable(ChooseRoutePage.TYPE_MOVEMENT(id))
        self.click(ChooseRoutePage.TYPE_MOVEMENT(id))

    @allure.step("Click on the button 'Вызвать такси'")
    def click_on_button_order_taxi(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.ORDER_TAXI_BUTTON
        )
        self.wait_element_clickable(
            ChooseRoutePage.ORDER_TAXI_BUTTON
        )
        self.click(ChooseRoutePage.ORDER_TAXI_BUTTON)

    def get_price_line_from_info_block(self):
        return self.get_text(ChooseRoutePage.PRICE_INFO_ROUTE)

    def get_price_from_info_block(self):
        price: str = self.get_price_line_from_info_block()
        return price.split('~')[1].strip().split()[0]

    def get_during_line_from_info_block(self):
        return self.get_text(ChooseRoutePage.DURING_INFO_ROUTE)

    def get_during_from_info_block(self):
        during: str = self.get_during_line_from_info_block()
        return during.split()[2]

    def is_car_type_active(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.TYPE_MOVEMENT(1)
        )

        return "disabled" not in self.get_attribute(
            ChooseRoutePage.TYPE_MOVEMENT(1), 'class'
        )

    def is_by_foot_type_active(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.TYPE_MOVEMENT(2)
        )

        return "disabled" not in self.get_attribute(
            ChooseRoutePage.TYPE_MOVEMENT(2), 'class'
        )

    def is_taxi_type_active(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.TYPE_MOVEMENT(3)
        )

        return "disabled" not in self.get_attribute(
            ChooseRoutePage.TYPE_MOVEMENT(3), 'class'
        )

    def is_on_byke_type_active(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.TYPE_MOVEMENT(4)
        )

        return "disabled" not in self.get_attribute(
            ChooseRoutePage.TYPE_MOVEMENT(4), 'class'
        )

    def is_on_scooter_type_active(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.TYPE_MOVEMENT(5)
        )

        return "disabled" not in self.get_attribute(
            ChooseRoutePage.TYPE_MOVEMENT(5), 'class'
        )

    def is_myself_type_active(self):
        self.wait_visibility_of_element_located(
            ChooseRoutePage.TYPE_MOVEMENT(6)
        )

        return "disabled" not in self.get_attribute(
            ChooseRoutePage.TYPE_MOVEMENT(6), 'class'
        )

    def are_types_active(self):
        return (
            self.is_car_type_active()
            and self.is_by_foot_type_active()
            and self.is_taxi_type_active()
            and self.is_on_byke_type_active()
            and self.is_on_scooter_type_active()
            and self.is_myself_type_active()
        )
