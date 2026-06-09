import allure

import data
import pages


@allure.feature('Tests for complited order window')
class TestComplitedOrderPage:

    @allure.title('Complited order has expected title')
    def test_complited_order_has_expected_title(self, ordered_taxi):
        complited_order_page = pages.ComplitedOrderPage(ordered_taxi)
        complited_order_page.wait_show_up_complited_order_page()

        assert True

    @allure.title('Complited order has car number and tariff image')
    def test_complited_order_has_car_number_and_tariff_image(
        self, ordered_taxi
    ):
        complited_order_page = pages.ComplitedOrderPage(ordered_taxi)
        complited_order_page.wait_show_up_complited_order_page()

        assert (complited_order_page.has_car_number()
                and complited_order_page.has_image_tariff())

    @allure.title('Complited order has raiting, name and foto driver')
    def test_complited_order_has_raiting_and_name_and_foto_driver(
        self, ordered_taxi
    ):
        complited_order_page = pages.ComplitedOrderPage(ordered_taxi)
        complited_order_page.wait_show_up_complited_order_page()

        assert (complited_order_page.has_raiting()
                and complited_order_page.has_image_tariff()
                and complited_order_page.has_car_driver_name())

    @allure.title('Complited order has expected detail')
    def test_complited_order_has_expected_detail(
        self, order_taxi_form
    ):
        order_taxi_page = pages.OrderTaxiForm(order_taxi_form)
        order_taxi_page.choose_tariff(data.TEST_TARIFF_NAME)
        expected_price = order_taxi_page.get_price_tariff(
            data.TEST_TARIFF_NAME
        )
        order_taxi_page.order_with_requirement_table()
        complited_order_page = pages.ComplitedOrderPage(
            order_taxi_page.driver
        )
        complited_order_page.wait_show_up_complited_order_page()
        complited_order_page.press_detail()

        assert (complited_order_page.get_prince_from_detail_page()
                == expected_price)

    @allure.title('After press on cancel button the complited page is closed')
    def test_complited_order_press_cancel_is_closed(
        self, ordered_taxi
    ):
        complited_order_page = pages.ComplitedOrderPage(ordered_taxi)
        complited_order_page.wait_show_up_complited_order_page()
        complited_order_page.press_cancel()

        assert complited_order_page.is_not_visible()
