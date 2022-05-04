from selenium.webdriver.common.by import By


class Locators:
    # login
    BUTTON_COOKIE = (By.XPATH, "//button[text()='Accept']")
    SIGN_IN = (By.XPATH, "//header/nav[1]/div[2]/div[6]")  # переделать
    INPUT_EMAIL_FIELD = (By.XPATH, "//input[@id='username']")
    BUTTON_CONTINUE_WITH_EMAIL = (By.XPATH, "//span[contains(text(),'Continue with email')]")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    BUTTON_SIGN_IN_PASSWORD = (By.XPATH, "//span[text()='Sign in']")
    BUTTON_PRESS_AND_HOLD = (By.XPATH, "//div[@aria-label='Press and hold']")

    # search
    TAB_ATTRACTIONS = (By.XPATH, "//span[contains(text(),'Attractions')]")
    INPUT_FIELD_FIND = (By.XPATH, "//input[@name='query']")
    CHECK_MUSEUMS = (By.XPATH, "//span[contains(text(),'Museums')]")
    LIST_RESULT_SEARCH = (By.XPATH, "//a[@class='css-aaudvs']")
    ELEMENT_TITLE_FIND = (By.XPATH, "//h2[@class='_5446b0d175 css-1uk1gs8']")
