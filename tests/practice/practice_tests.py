from pages.practice.practicepage import PracticePage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("one_time_setup", "set_up")
class Practice_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.pp = PracticePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_radio_bmw_selected(self):
        result = self.pp.radio_button_bmw()
        self.ts.mark_final("test_verify_radio_bmw_selected", result, "radio button bmw selection")
        self.ts.screen_shot("radio_button_bmw_is_selected")
        assert True

    @pytest.mark.run(order=2)
    def test_verify_radio_honda_selected(self):
        result = self.pp.radio_button_honda()
        self.ts.mark_final("test_verify_radio_honda_selected", result, "radio button honda selection")
        self.ts.screen_shot("radio_button_honda_is_selected")
        assert True

    @pytest.mark.run(order=3)
    def test_verify_radio_benz_selected(self):
        result = self.pp.radio_button_benz()
        self.ts.mark_final("test_verify_radio_benz_selected", result, "radio button benz selection")
        self.ts.screen_shot("radio_button_benz_is_selected")
        assert True

    @pytest.mark.run(order=4)
    def test_verify_checkboxes_selected(self):
        result1 = self.pp.checkbox_benz()
        result2 = self.pp.checkbox_honda()
        result3 = self.pp.checkbox_bmw()
        self.ts.mark_final("test_verify_checkboxes_selected", result1, "checkbox benz selection")
        self.ts.mark_final("test_verify_checkboxes_selected", result2, "checkbox honda selection")
        self.ts.mark_final("test_verify_checkboxes_selected", result3, "checkbox bmw selection")
        self.ts.screen_shot("test_verify_checkboxes_selected")
        assert True

    @pytest.mark.run(order=5)
    def test_select_honda(self):
        self.pp.select_honda()
        result = self.pp.verify_selection()
        self.ts.mark_final("test_select_honda", result, "select drop down honda")
        self.ts.screen_shot("test_select_honda")
        assert True

    @pytest.mark.run(order=6)
    def test_select_bmw(self):
        self.pp.select_bmw()
        result = self.pp.verify_selection()
        self.ts.mark_final("test_select_bmw", result, "select drop down bmw")
        self.ts.screen_shot("test_select_bmw")
        assert True

    @pytest.mark.run(order=7)
    def test_select_benz(self):
        self.pp.select_benz()
        result = self.pp.verify_selection()
        self.ts.mark_final("test_select_benz", result, "select drop down benz")
        self.ts.screen_shot("test_select_benz")
        assert True


