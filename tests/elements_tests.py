from pages.element_page import TestAttractions


class TestElements:

    def test(self, driver):
        test = TestAttractions(driver, "https://www.booking.com/index.en-gb.htm")
        test.open()
        test.cookie()
        # test.log_in()
        title_find = test.test_check_museums()
        text_web_element_title = test.find_actual_title()
        assert text_web_element_title == title_find

