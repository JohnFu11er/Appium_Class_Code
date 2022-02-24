from appium.webdriver.common.appiumby import AppiumBy


class WelcomeWindow:
    # region Objects
    def __init__(self, driver):
        self.driver = driver

        self.return_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6")
        self.close_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "7")
        self.portal_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17")
    # endregion

    # region Methods
    def go_to_portal(self):
        self.portal_button.click()

    def back_to_login(self):
        self.return_button.click()

    def exit_application(self):
        self.close_button.click()
    # endregion
