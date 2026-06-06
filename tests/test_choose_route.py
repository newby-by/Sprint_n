import allure
import pytest

import data
import pages


@allure.feature("Choose a route")
class TestChooseRoute:

    @allure.title("The block with types is shown up")
    @allure.description("After filling addresses up with different ones")
    def test_show_type_block_with_different_addresses(
        self, route_with_different_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
        assert chose_route_page.is_type_block_available()

    @allure.title("Expected info text in types is shown")
    @allure.description("Expected text after filling addresses up "
                        "with the same ones")
    def test_show_type_block_with_different_addresses_and_expected_text(
        self, route_with_the_same_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_the_same_addresses
        )
        assert chose_route_page.is_info_with_the_same_addresses_correct()
    
    @allure.title("Choose an optimal route with different addreses")
    def test_choose_optimal_route_with_different_addresses(
        self, route_with_different_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
        chose_route_page.choose_optimal_route()

        assert (chose_route_page.is_optimal_route_available()
                and chose_route_page.is_info_about_optimal_route_correct())

    @allure.title("Choose a rapid route with different addreses")
    def test_choose_rapid_route_with_different_addresses(
        self, route_with_different_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
        chose_route_page.choose_rapid_route()

        assert (chose_route_page.is_rapid_route_available()
                and chose_route_page.is_info_about_rapid_route_correct())
    
    @pytest.mark.xfail(reason='During is not different', strict=True)
    def test_switch_from_optimal_to_radid_info_is_changed(
        self, route_with_different_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
        chose_route_page.choose_optimal_route()
        optimal_info = (chose_route_page.get_price_from_info_block(),
                        chose_route_page.get_during_from_info_block())

        chose_route_page.choose_rapid_route()
        rapid_info = (chose_route_page.get_price_from_info_block(),
                        chose_route_page.get_during_from_info_block())

        assert (
            optimal_info[0] != rapid_info[0]
            and optimal_info[1] != rapid_info[1]
            and chose_route_page.is_rapid_route_available()
            and not chose_route_page.is_optimal_route_available()
        ), (
            f"{optimal_info} or {rapid_info} are not different.\n"
            f"Active rapid= {chose_route_page.is_rapid_route_available()}"
            f"Active optimal= {chose_route_page.is_optimal_route_available()}"
        )

    @allure.title("Choose a myself route with different addreses")
    @allure.description("The types are active")
    def test_choose_myself_route_with_different_addresses_types_active(
        self, route_with_different_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
        chose_route_page.choose_myself_route()

        assert chose_route_page.are_types_active()

    @allure.title("Choose a myself route with different addreses")
    @allure.description("The button 'Забронировать' is active for type 'Драйв'")
    def test_choose_myself_route_with_different_addresses_with_carsharing(
        self, route_with_different_addresses
    ):
        chose_route_page = pages.ChooseRoutePage(
            route_with_different_addresses
        )
        chose_route_page.choose_myself_route()
        chose_route_page.choose_type_with(data.TYPE_MOVEMENT['Драйв'])

        assert chose_route_page.is_info_about_rapid_route_correct_with_carsharing()
