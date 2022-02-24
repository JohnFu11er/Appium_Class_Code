from appium.webdriver.common.appiumby import AppiumBy


class ErrorWindow:
    # region Objects
    def __init__(self, driver):
        self.driver = driver
        self.okButton = self.driver.find_element(AppiumBy.NAME, "OK")
    # endregion

    # region Methods
    def clear_error(self):
        self.okButton.click()
    # endregion
