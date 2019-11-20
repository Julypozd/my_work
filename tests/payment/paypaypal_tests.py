from pages.payment.paymentpage import PaymentPage
from pages.home.loginpage import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.courses = PaymentPage(self.driver)
        self.lp= LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_invalid_enrollment(self):
        self.lp.login("test@email.com", "abcabc")
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_validLogin", result2, "Login Verification")
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_topay()
        self.courses.enroll_java_paypal()
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalidenrollment", result, "Enrollment Failed")
        assert result == True

