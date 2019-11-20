from pages.courses.courses_page import CoursesPage
from pages.home.loginpage import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("one_time_setup", "set_up")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.courses = CoursesPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("test@email.com", "abcabc"))
    @unpack
    def test_valid_login(self, email, password):
        self.lp.login(email, password)
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_validLogin", result2, "Login Verification")

    @pytest.mark.run(order=2)
    @data(("JavaScript for beginners", '0000 0000 0000 0000', "2305", "123", 27560),
          ("Selenium WebDriver With Java", '0000 0000 0000 0000', "2305", "123", 27560))
    @unpack
    def test_invalid_enrollments(self, cource_name, card_num, exp_date, cvc_num, zip_code):
        self.courses.enter_course_name(name=cource_name)
        self.courses.select_course_topay()
        self.courses.enroll_java_visa(cardnum=card_num, expdate=exp_date, cvc=cvc_num, zip=zip_code)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed")
        self.courses.click_all_courses()
        assert True
