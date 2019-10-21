from pages.payment.payment_page import Payment_page
from pages.home.loginpage import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = Payment_page(self.driver)
        self.lp= LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    def test_invalidEnrollment(self):
        self.lp.login("test@email.com", "abcabc")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_topay()
        self.courses.enroll_java_visa(cardnum='1234 4555 5432 1234', expdate="2305", cvc="123", zip=27560)
        result =self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidenrollment", result, "Enrollment Failed")
        assert result== True