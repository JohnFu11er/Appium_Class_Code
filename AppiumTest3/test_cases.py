from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestCases:
    # region Appium Session Info
    desired_cap = {
        "platformName": "Windows",
        "deviceName": "WindowsPC",
        "app": r"C:\Windows\System32\win32calc.exe"
    }
    link = "http://127.0.0.1:4723"
    # endregion

    # region Setup
    def setup_method(self):
        self.calculator_session = webdriver.Remote(self.link, self.desired_cap)
    # endregion

    # region Tests
    def test_1(self):
        self.calculator_session.find_element(AppiumBy.NAME, "6").click()
        self.calculator_session.find_element(AppiumBy.NAME, "3").click()
        self.calculator_session.find_element(AppiumBy.ACCESSIBILITY_ID, "94").click()
        self.calculator_session.find_element(AppiumBy.ACCESSIBILITY_ID, "135").click()
        self.calculator_session.find_element(AppiumBy.ACCESSIBILITY_ID, "121").click()

    def test_2(self):
        self.calculator_session.find_element(AppiumBy.NAME, "7").click()
        self.calculator_session.find_element(AppiumBy.NAME, "Subtract").click()
        self.calculator_session.find_element(AppiumBy.NAME, "3").click()
        self.calculator_session.find_element(AppiumBy.NAME, "Equals").click()

        result = self.calculator_session.find_element(AppiumBy.NAME, 'Result').text
        assert int(result) == 4

    def test_3(self):
        self.calculator_session.find_element(AppiumBy.NAME, "5").click()
        self.calculator_session.find_element(AppiumBy.NAME, "1").click()
        self.calculator_session.find_element(AppiumBy.XPATH, "//Window[@ClassName=\"CalcFrame\"][@Name=\"Calculator\"]/Pane[@ClassName=\"CalcFrame\"]/Button[@ClassName=\"Button\"][@Name=\"Clear\"]"
).click()
    # endregion

    # region Teardown
    def teardown_method(self):
        self.calculator_session.quit()
    # endregion