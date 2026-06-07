import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class  WaitPage(BasePage):

    TITLE = (By.XPATH, ".//div[text()='Поиск машины']")
    TIME = (
        By.XPATH, ".//div[text()='Поиск машины']/following-sibling::div"
    )
    CANCEL_BUTTON = (
        By.XPATH, ".//div[text()='Отменить']/preceding-sibling::button"
    )
    DETAIL_BUTTON = (
        By.XPATH, ".//div[text()='Детали']/preceding-sibling::button"
    )

    def is_available(self):
        self.wait_visibility_of_element_located(WaitPage.TITLE)
        self.wait_text_in_element(WaitPage.TIME, lambda text: text)
        self.wait_text_in_element_is_changed(
            WaitPage.TIME,
            self.find_element(WaitPage.TIME).text
        )
        self.wait_element_clickable(WaitPage.CANCEL_BUTTON)
        self.wait_element_clickable(WaitPage.DETAIL_BUTTON)
        return True
    
    @allure.step("Press the cancel button")
    def press_cancel(self):
        self.click(WaitPage.CANCEL_BUTTON)

    @allure.step("Press the detail button")
    def press_detail(self):
        self.click(WaitPage.DETAIL_BUTTON)
