import os
import pytest
import psutil
import pandas as pd
from appium import webdriver
from Pages.login_page import LoginWindow
from Pages.error_page import ErrorWindow
from Pages.welcome_page import WelcomeWindow
from Pages.verification_page import VerificationWindow
from Pages.portal_page import PortalPage
from Keywords.keywords import LowLevelKeywords


class TestCases:
    app_settings_session = None
    appium_session = None

    # region CSV Reader
    @staticmethod
    def get_test_data():
        df = pd.read_csv(r"C:\Users\Administrator\Documents\Appium Python Training\PageObjectModel\Data\test_case_data.csv", index_col=0)

        for i, row in df.iterrows():
            step = str(row[0])
            page = str(row[1])
            object = str(row[2])
            keyword = str(row[3])
            value = str(row[4])
            yield step, page, object, keyword, value
    # endregion

    # region Test Report
    @staticmethod
    def report_summary(step, page, element, keyword, value):
        print(step)
        print(f"Page {page}")
        print(f"Action: {keyword} on {element}")
        print(f"Value: {value}")
    # endregion

    # region Tests
    # region Standard Tests
    # @pytest.mark.order(1)
    # def test_login(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #
    #
    # @pytest.mark.order(2)
    # def test_return(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.return_to_main()
    #
    #
    # @pytest.mark.order(3)
    # def test_exit(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.exit_application()
    #
    # @pytest.mark.order(4)
    # @pytest.mark.parametrize("username,password", [("username1", "password1"), ("username2", "password2")])
    # def test_failed_login(self, username, password):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_failure(username, password)
    #     self.error_page = ErrorWindow(self.app_settings_session)
    #     self.error_page.clear_error()
    #
    # @pytest.mark.order(5)
    # def test_verification(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.exit_application()
    #
    # @pytest.mark.order(6)
    # @pytest.mark.parametrize("code", ["1245", "1111"])
    # def test_failed_verification(self, code):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_failure(code)
    #     self.error_page = ErrorWindow(self.app_settings_session)
    #     self.error_page.clear_error()
    #
    # @pytest.mark.order(7)
    # def test_link_1(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.go_to_portal()
    #     self.portal_page = PortalPage(self.app_settings_session)
    #     self.portal_page.link_1_verify()
    #
    # @pytest.mark.order(8)
    # def test_link_2(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.go_to_portal()
    #     self.portal_page = PortalPage(self.app_settings_session)
    #     self.portal_page.link_2_verify()
    #
    # @pytest.mark.order(9)
    # def test_link_3(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.go_to_portal()
    #     self.portal_page = PortalPage(self.app_settings_session)
    #     self.portal_page.link_3_verify()
    #
    # @pytest.mark.order(10)
    # def test_link_4(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.go_to_portal()
    #     self.portal_page = PortalPage(self.app_settings_session)
    #     self.portal_page.link_4_verify()
    #
    # @pytest.mark.order(11)
    # def test_portal_exit(self):
    #     self.login_page = LoginWindow(self.app_settings_session)
    #     self.login_page.login_to_application()
    #     self.verification_page = VerificationWindow(self.app_settings_session)
    #     self.verification_page.verify_successfully()
    #     self.welcome_page = WelcomeWindow(self.app_settings_session)
    #     self.welcome_page.go_to_portal()
    #     self.portal_page = PortalPage(self.app_settings_session)
    #     self.portal_page.exit_application()
    # endregion

    # region Keyword Tests
    # @pytest.mark.parametrize("page,element,keyword,value", [("LoginWindow", "username_field", "EnterData", "john")])
    @pytest.mark.parametrize("step,page,element,keyword,value", get_test_data())
    def test_kwf(self, step, page, element, keyword, value):
        class_type = globals()[page]
        class_instance = class_type(self.app_settings_session)
        get_prop_info = getattr(class_instance, element)
        self.keyword_class = LowLevelKeywords()
        self.keyword_class.process_keywords(keyword, get_prop_info, value)
        self.report_summary(step, page, element, keyword, value)
    # endregion

    # endregion

    # region Setup
    @classmethod
    def setup_class(cls):
        os.startfile(r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe")
        keyword_class = LowLevelKeywords()

        app_path = r"C:\Users\Administrator\Documents\Appium Python Training\LoginWPFApp\bin\debug\LoginWPFApp.exe"
        session_link = "http://127.0.0.1:4723"
        desired_cap = {
            'platformName': "Windows",
            'deviceName': "WindowsPC",
            'app': app_path
        }
        desired_cap_root = {
            'app': "Root"
        }

        cls.appium_session = webdriver.Remote(session_link, desired_cap)
        cls.app_settings_session = webdriver.Remote(session_link, desired_cap_root)
        # cls.appium_session.close_app()

    # def setup_method(self):
    #     self.appium_session.launch_app()

    # endregion

    # region Teardown
    @classmethod
    def teardown_class(cls):
        cls.app_settings_session.close_app()

        app_list = psutil.pids()
        for i in range(0, len(app_list)):
            try:
                p = psutil.Process(app_list[1])
                if p.cmdline()[0].find(r"C:\Users\Administrator\Documents\Appium Python "
                                       r"Training\LoginWPFApp\bin\debug\LoginWPFApp.exe") != -1:
                    p.kill()
                elif p.cmdline()[0].find(r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe") != -1:
                    p.kill()

            except:
                pass

    # def teardown_method(self):
    #     self.app_settings_session.close_app()

    # endregion
