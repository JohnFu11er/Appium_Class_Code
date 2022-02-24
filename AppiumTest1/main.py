from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException

desired_capabilities = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": r"C:\Windows\System32\Notepad.exe"
}

notepad_session = webdriver.Remote("http://127.0.0.1:4723", desired_capabilities)

try:
    notepad_session.find_element(AppiumBy.NAME, "Format").click()
    notepad_session.find_element(AppiumBy.NAME, "Font...").click()
    notepad_session.find_element(AppiumBy.ACCESSIBILITY_ID, "1001").send_keys("DejaVu Sans")
    notepad_session.find_element(AppiumBy.NAME, "Bold").click()
    notepad_session.find_element(AppiumBy.NAME, "18").click()
    notepad_session.find_element(AppiumBy.ACCESSIBILITY_ID, "1").click()
except WebDriverException as e:
    print("App not started.")
    print(e)
finally:
    notepad_session.quit()
