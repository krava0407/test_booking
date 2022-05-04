import time

from selenium.webdriver.common.keys import Keys

from locators.locator_page import Locators
from pages.base_page import BasePage


class TestAttractions(BasePage):
    locators = Locators

    def cookie(self):
        """method for cookies"""
        self.element_is_visible(self.locators.BUTTON_COOKIE).click()

    def log_in(self):
        """method for logging on the site, but he not works, because the site has a check from bots"""
        self.element_is_visible(self.locators.SIGN_IN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.INPUT_EMAIL_FIELD).send_keys(self.EMAIL)
        time.sleep(3)
        self.element_is_visible(self.locators.BUTTON_CONTINUE_WITH_EMAIL).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(self.PASSWORD)
        time.sleep(3)
        self.element_is_visible(self.locators.BUTTON_SIGN_IN_PASSWORD).click()
        time.sleep(30)

    def test_check_museums(self):
        """method that implements the following tasks:
            - Press “Attractions” tab
            - Search by keyword “travel”
            - Press “Museums” checkbox
            - returns title of the first element from the list of links
            """
        museum = True
        while museum:
            self.element_is_visible(self.locators.TAB_ATTRACTIONS).click()
            time.sleep(1)
            self.element_is_visible(self.locators.INPUT_FIELD_FIND).send_keys(self.KEY_SEARCH)
            time.sleep(1)
            self.element_is_visible(self.locators.INPUT_FIELD_FIND).send_keys(Keys.ENTER)
            time.sleep(1)
            try:
                self.element_is_visible(self.locators.CHECK_MUSEUMS)
                museum = False
            except:
                print('Museum not found')
                self.open()

        self.element_is_visible(self.locators.CHECK_MUSEUMS).click()
        search_list = self.element_are_presence(self.locators.LIST_RESULT_SEARCH)
        url = search_list[0].get_attribute("href")
        title_find = search_list[0].get_attribute("title")
        self.open_search_page(url=url)
        return title_find

    def find_actual_title(self):
        """method returns title opened page"""
        web_element_title = self.element_are_presence(self.locators.ELEMENT_TITLE_FIND)
        text_web_element_title = web_element_title[0].text
        return text_web_element_title


