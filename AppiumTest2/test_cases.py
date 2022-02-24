import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AllTestCases(unittest.TestCase):
    desired_cap = {
        "platformName": "Windows",
        "deviceName": "WindowsPC",
        "app": r"C:\Windows\System32\Notepad.exe",
        "appArguments": r"C:\Users\Administrator\Desktop\AppiumText.txt"
    }
    link = "http://127.0.0.1:4723"

    def setUp(self):
        self.notepad_session = webdriver.Remote(self.link, self.desired_cap)

    def test_1(self):
        self.notepad_session.find_element(AppiumBy.CLASS_NAME, "Edit").send_keys("John test")
        self.notepad_session.find_element(AppiumBy.NAME, "Edit").click()

    def tearDown(self):
        self.notepad_session.quit()


if __name__ == '__main__':
    unittest.main()