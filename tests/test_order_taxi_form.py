import allure
import pytest

import data
import pages


@allure.feature("Order a taxi")
class TestOrderTaxi:

    @allure.title("Check the page of taxi ordering is available")
    def test_order_form_available(self, order_taxi_form):
        order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
        assert order_taxi_page.is_available()

    @allure.title("The form order taxi has 6 cards")
    def test_order_form_has_6_tariffs(self, order_taxi_form):
        order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
        assert (order_taxi_page.get_card_numbers()
                == len(data.ORDER_TAXI_FORM['tariffs']))

    @allure.title("The form order taxi has only one active card")
    def test_order_form_has_only_1_active(self, order_taxi_form):
        order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
        assert order_taxi_page.is_only_1_card_active()

    @allure.title("The order form has expected fields")
    def test_order_form_has_expected_fields(self, order_taxi_form):
        order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
        assert order_taxi_page.has_4_fields_in_form()
        
    @allure.title("The tariff {tariff_title} has expected description")
    @pytest.mark.parametrize("tariff_title", data.ORDER_TAXI_FORM["params"])
    def test_tariff_has_expected_description(self, order_taxi_form, tariff_title):
        order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
        order_taxi_page.choose_tariff(tariff_title)
        order_taxi_page.open_description_tariff_with(tariff_title)
        assert order_taxi_page.has_expected_description(tariff_title)
