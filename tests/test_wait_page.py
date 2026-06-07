import allure

import pages


@allure.feature('Tests for wait window')
class TestWaitPage:

    @allure.title('After ordered taxi wait form is available')
    def test_wait_page_arter_odered_is_available(swelf, ordered_taxi):
        wait_page = pages.WaitPage(ordered_taxi)

        assert wait_page.is_available()
