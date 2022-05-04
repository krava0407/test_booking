from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    EMAIL = "testbooking22@gmail.com"
    PASSWORD = "werf34QWE@"
    KEY_SEARCH = "travel"

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(driver=self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=10):
        return wait(driver=self.driver, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_are_presence(self, locator, timeout=10):
        return wait(driver=self.driver, timeout=timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_presence(self, locator, timeout=10):
        return wait(driver=self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(driver=self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def open_search_page(self, url):
        self.driver.get(url)
