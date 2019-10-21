from pages.home.loginpage import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_verifytitle(self):
        result1=self.lp.verifyLoginTitle()
        self.ts.markFinal("test_verifytitle", result1, "Title verified")
        self.ts.screenShot("title verified")

    @pytest.mark.run(order=2)
    def test_invalid_password(self):
        self.lp.login(email="test@email.com", password="abcabca")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalid_password", result, "Invalid password->login is invalid")
        self.ts.screenShot("test_invalid_password")
        assert True

    @pytest.mark.run(order=3)
    def test_invalid_email(self):
        self.lp.login(email="test@mail.com", password="abcabca")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalid_email", result, "Invalid email -> login is invalid")
        self.ts.screenShot("test_invalid_email")
        assert True

    @pytest.mark.run(order=4)
    def test_invalid_login(self):
        self.lp.login(email="test@mail.com", password="abcabcaa")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalid_login", result, "Invalid credentials -> login is invalid")
        self.ts.screenShot("test_invalid_login")
        assert True


    @pytest.mark.run(order=5)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")
        self.ts.screenShot("login successfully")

    @pytest.mark.run(order=6)
    def test_logOut(self):
        result3 = self.lp.verifyLogOut()
        self.ts.markFinal("test_logOut", result3, "logout successfully")
        self.ts.screenShot("logout successfully")