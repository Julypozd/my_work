import utilities.logfile as logf
import logging
from base.base_methods import Base_methods

class Practice_page(Base_methods):

    log = logf.logfile(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

                    # Locators
    #Practice page link
    _practice_link = "//a[@class='fedora-navbar-link navbar-link']"
    #Radio Buttons
    _radio_button_bmw = "bmwradio"
    _radio_button_benz = "benzradio"
    _radio_button_honda = "hondaradio"
    #Select Class
    _select_menu = "carselect"
    _select_bmw = "bmw" #value
    _select_benz = 1 #index
    _select_honda = "Honda" #text
    # Checkboxes
    _checkbox_bmw = "bmwcheck"
    _checkbox_honda = "benzcheck"
    _checkbox_benz = "hondacheck"
    # Multiple Select
    _apple = ""
    _orange = ""
    _peach = ""
    #_Switch Window
    #_Switch Tab
    #_Switch To Alert
    _verify_sel = "//div[@id='checkbox-example']//label[1]"

    def radio_button_bmw(self):
        self.click_element(self._practice_link, locator_type="xpath")
        self.click_element(self._radio_button_bmw, locator_type="id")
        result = self.is_element_selected(locator=self._radio_button_bmw, locator_type="id")
        return result

    def radio_button_benz(self):
        self.click_element(self._radio_button_benz, locator_type="id")
        result = self.is_element_selected(locator=self._radio_button_benz, locator_type="id")
        return result

    def radio_button_honda(self):
        self.click_element(self._radio_button_honda, locator_type="id")
        result = self.is_element_selected(locator=self._radio_button_honda, locator_type="id")
        return result

    def checkbox_bmw(self):
        self.click_element(self._checkbox_bmw, locator_type="id")
        result = self.is_element_selected(locator=self._checkbox_bmw, locator_type="id")
        return result

    def checkbox_benz(self):
        self.click_element(self._checkbox_benz, locator_type="id")
        result = self.is_element_selected(locator=self._checkbox_benz, locator_type="id")
        return result

    def checkbox_honda(self):
        self.click_element(self._checkbox_honda, locator_type="id")
        result = self.is_element_selected(locator=self._checkbox_honda, locator_type="id")
        return result

    def select_honda(self):
        element_menu = self.get_element(locator=self._select_menu, locator_type="id")
        result = self.select_element_dropdown_by(element=element_menu, text=self._select_honda)
        return result

    def select_bmw(self):
        element_menu = self.get_element(locator=self._select_menu, locator_type="id")
        result = self.select_element_dropdown_by(element=element_menu, value=self._select_bmw)
        return result

    def select_benz(self):
        element_menu = self.get_element(locator=self._select_menu, locator_type="id")
        result = self.select_element_dropdown_by(element=element_menu, index=self._select_benz)
        return result

    def verify_selection(self):
        result = self.is_element_present(locator=self._verify_sel, locator_type="xpath")
        return result

