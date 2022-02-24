from appium.webdriver.common.appiumby import AppiumBy


class LoginWindow:
    # region Objects
    def __init__(self, driver):
        self.driver = driver

        self.username_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1")
        self.password_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2")
        self.login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3")
        self.clear_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "4")
        self.close_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5")
    # endregion

    # region Methods
    def login_to_application(self):
        self.username_field.send_keys("john")
        self.password_field.send_keys("password")
        self.login_button.click()

    def login_failure(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        username_text = self.username_field.text
        self.login_button.click()
        return username_text

    def exit_application(self):
        self.close_button.click()


    # endregion
