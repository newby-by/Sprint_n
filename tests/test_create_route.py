import allure

import data
import pages


@allure.feature("Create a route")
class TestCreateRoute:

    @allure.title("Create a route with different addreses")
    def test_create_route_with_different_addresses(self, driver):
        create_route = pages.CreateRoutePage(driver)
        create_route.open(data.BASE_URL)
        create_route.set_start_route(data.ADDRESSES[0])
        create_route.set_end_route(data.ADDRESSES[1])

        assert (create_route.is_address_available(data.ADDRESSES[0])
                and create_route.is_address_available(data.ADDRESSES[1]))
