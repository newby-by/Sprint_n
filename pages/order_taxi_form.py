from selenium.webdriver.common.by import By

import data
from .base_page import BasePage


class OrderTaxiForm(BasePage):
    ORDER_TAXI_BUTTON = (
        By.XPATH, ".//span[text()='Ввести номер и заказать']"
    )
    CARDS = (
        By.XPATH, ".//div[@class='tariff-cards']/child::div"
    )
    CARD_BY_TITLE = lambda title: (
        By.XPATH,
        (".//div[@class='tariff-cards']//div[@class='tcard-title' and "
         f"text()='{title}']/parent::div")
    )
    INFO_BUTTON = lambda title: (
        OrderTaxiForm.CARD_BY_TITLE(title)[0],
        OrderTaxiForm.CARD_BY_TITLE(title)[1] + "/button"
    )
    FIELDS = (
        By.XPATH, ".//div[@class='form']/div"
    )
    TARIFF_DESCRIPTION = lambda id: (
        By.XPATH,
        f".//div[@id='tariff-card-{id}']//div[@class='i-dPrefix']"
    )

    def is_available(self):
        self.wait_visibility_of_element_located(
            OrderTaxiForm.ORDER_TAXI_BUTTON
        )
        self.wait_element_clickable(
            OrderTaxiForm.ORDER_TAXI_BUTTON
        )
        return True

    def get_card_numbers(self):
        return len(self.find_elements(OrderTaxiForm.CARDS))
    
    def get_card_by_title(self, title):
        self.wait_visibility_of_element_located(
            OrderTaxiForm.CARD_BY_TITLE(title)
        )
        return self.find_element(OrderTaxiForm.CARD_BY_TITLE(title))
    
    def is_card_active(self, title):
        card = self.get_card_by_title(title)
        return "active" in card.get_attribute('class')
    
    def is_only_1_card_active(self):
        return sum(map(
            lambda title: int(self.is_card_active(title)),
            list(data.ORDER_TAXI_FORM['tariffs'])
        )) == data.ONLY_ONE_CARD_ACTIVE

    def has_4_fields_in_form(self):
        self.wait_visibility_of_element_located(OrderTaxiForm.FIELDS)
        are_cards = [title in card.text 
                     for card, title in zip(
                         self.find_elements(OrderTaxiForm.FIELDS),
                         data.ORDER_TAXI_FORM['fields'])
                    ]
        return (
            all(are_cards)
            and len(are_cards) == len(data.ORDER_TAXI_FORM['fields'])
        )
    
    def has_expected_description(self, title):
        id = data.ORDER_TAXI_FORM["tariffs"].index(title)
        return self.get_text(
            OrderTaxiForm.TARIFF_DESCRIPTION(id)
        ) == data.ORDER_TAXI_FORM["descriptions"][id]
    
    def choose_tariff(self, title):
        self.click(OrderTaxiForm.CARD_BY_TITLE(title))

    def open_description_tariff_with(self, title):
        locator = OrderTaxiForm.INFO_BUTTON(title)
        self.wait_element_clickable(locator)
        self.move_cursor_to(locator)
