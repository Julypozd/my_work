from pages.home.login_page import Login_page
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Login_page(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_verifytitle(self):
        result1 = self.lp.verify_login_title()
        self.ts.mark_final("test_verifytitle", result1, "Title verified")
        self.ts.screen_shot("title verified")

    @pytest.mark.run(order=2)
    def test_invalid_password(self):
        self.lp.login(email="test@email.com", password="abcabca")
        result = self.lp.verify_login_failed()
        self.ts.mark_final("test_invalid_password", result, "Invalid password->login is invalid")
        self.ts.screen_shot("test_invalid_password")
        assert True

    @pytest.mark.run(order=3)
    def test_invalid_email(self):
        self.lp.login(email="test@mail.com", password="abcabca")
        result = self.lp.verify_login_failed()
        self.ts.mark_final("test_invalid_email", result, "Invalid email -> login is invalid")
        self.ts.screen_shot("test_invalid_email")
        assert True

    @pytest.mark.run(order=4)
    def test_invalid_login(self):
        self.lp.login(email="test@mail.com", password="abcabcaa")
        result = self.lp.verify_login_failed()
        self.ts.mark_final("test_invalid_login", result, "Invalid credentials -> login is invalid")
        self.ts.screen_shot("test_invalid_login")
        assert True

    @pytest.mark.run(order=5)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_validLogin", result2, "Login Verification")
        self.ts.screen_shot("login successfully")
        assert True

    @pytest.mark.run(order=6)
    def test_log_out(self):
        result3 = self.lp.verify_log_out()
        self.ts.mark_final("test_logOut", result3, "logout successfully")
        self.ts.screen_shot("logout successfully")
        assert True
