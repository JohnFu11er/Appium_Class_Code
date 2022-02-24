from appium.webdriver.common.appiumby import AppiumBy

class PortalPage:
    # region Objects
    def __init__(self, driver):
        self.driver = driver
        self.link_1_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12")
        self.link_2_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "13")
        self.link_3_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14")
        self.link_4_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "15")
        self.exit_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "16")
    # endregion

    # region Methods
    def link_1_verify(self):
        self.link_1_button.click()

    def link_2_verify(self):
        self.link_2_button.click()

    def link_3_verify(self):
        self.link_3_button.click()

    def link_4_verify(self):
        self.link_4_button.click()

    def exit_application(self):
        self.exit_button.click()
    # endregion
