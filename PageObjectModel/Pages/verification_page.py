from appium.webdriver.common.appiumby import AppiumBy


class VerificationWindow:
    # region Objects
    def __init__(self, driver):
        self.driver = driver

        self.code_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "9")
        self.continue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10")
        self.return_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "11")
    # endregion

    # region Methods
    def verify_successfully(self):
        self.code_field.send_keys("1234")
        self.continue_button.click()

    def verify_failure(self, code):
        self.code_field.send_keys(code)
        self.continue_button.click()

    def return_to_main(self):
        self.return_button.click()
    # endregion
