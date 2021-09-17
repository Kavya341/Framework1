import pytest
import unittest

from pages.LandingScreen import LandingScreen
from pages.LoginScreen import LoginScreen


@pytest.mark.usefixtures("get_driver")
class TestLogin(unittest.TestCase):

    # def test_aetUp(self):
    #     # self.driver.implicitly_wait(10)
    #     self.login_screen = LoginScreen(self.driver)
    #     self.landing_screen = LandingScreen(self.driver)

    def test_InvalidEmailAndPwd(self):
        self.login_screen = LoginScreen(self.driver)
        self.landing_screen = LandingScreen(self.driver)
        self.driver.implicitly_wait(10)
        self.login_screen.enter_email("test")
        self.driver.implicitly_wait(10)
        self.login_screen.enter_password("test")
        self.driver.implicitly_wait(10)
        self.login_screen.click_login()
        self.driver.implicitly_wait(10)
        self.assertEqual(self.login_screen.get_error(), 'Enter a valid Email ID and Password.')

