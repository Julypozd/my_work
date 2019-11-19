from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.logfile as log
import logging
import time
import os
from selenium.webdriver.support.ui import Select


class Custom_driver():

    log = log.logfile(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):

        file_name = result_message + "." + str(round(time.time() * 500)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        screenshot_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("### Exception occurred when taking screenshot")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type +
                          " not supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locator type: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locator type: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="id"):

        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("List of elements found with locator: " + locator +
                          " and  locator type: " + locator_type)
        except:
            self.log.info("List of elements NOT FOUND with locator: " + locator +
                          " and  locator type: " + locator_type)
        return element

    def click_element(self, locator="", locator_type="id", element=None):

        try:
            if locator is not None:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locator type: " + locator_type)
        except:
            self.log.info("CANNOT CLICK on the element with locator: " + locator +
                          " locator type: " + locator_type)
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):

        try:
            def get_text(self, locator="", locator_type="id", element=None, info=""):

                if locator is not None:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data: <" + data + "> on element with locator: " + locator +
                          " locator type: " + locator_type)
        except:
            self.log.info("CAN NOT SEND DATA on the element with locator: " + locator +
                  " locator type: " + locator_type)
            print_stack()



        try:
            if locator is not None:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("inner text")
            if len(text) != 0:
                self.log.info(" Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("FAILED to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type="id", element=None):

        try:
            if locator is not None:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element is present with locator: " + locator +
                              " locator type: " + locator_type)
                return True
            else:
                self.log.info("Element is not present with locator: " + locator +
                              " locator type: " + locator_type)
                return False
        except:
            print("Element NOT FOUND")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):

        is_displayed = False
        try:
            if locator is not None:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locator type: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locator type: " + locator_type)
            return is_displayed
        except:
            print("Element NOT FOUND")
            return False

    def elements_presence_check(self, locator, by_type):

        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locator type: " + str(by_type))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locator type: " + str(by_type))
                return False
        except:
            self.log.info("Element NOT FOUND")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element NOT appeared on the web page")
            print_stack()
        return element

    def scroll_page(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 800);")

    def swich_frame(self, framenumber):
        try:
            self.driver.switch_to.frame(framenumber)
            print("Switched to iframe num: " + framenumber)
        except:
            print("CAN NOT SWITCH iframe")

    def switch_to_frame(self, id="", name="", index=None):

        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_to_default_content(self):

        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator="", locator_type="id"):

        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
        value = element.get_attribute(attribute)
        return value

    def is_enabled(self, locator, locator_type="id", info=""):

        element = self.get_element(locator, locator_type=locator_type)
        enabled = False
        try:
            attributeValue = self.get_element_attribute_value(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info("Attribute value from application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def is_element_selected(self, locator="", locator_type="id", element=None):

        try:
            if locator is not None:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_el_selected = element.is_selected()
                if is_el_selected == True:
                    self.log.info("Element is selected with locator: " + locator +
                              " locator type: " + locator_type)
                    return True
                else:
                    self.log.info("Element is not selected with locator: " + locator +
                              " locator type: " + locator_type)
                    return False
            else:
                self.log.info("Element is not selected with locator: " + locator +
                             " locator type: " + locator_type)
        except:
            print("Element NOT FOUND")
            return False

    def select_element_dropdown_by(self, element, text="", value="", index=None):

        if text:
            return Select(element).select_by_visible_text(text)
        elif value:
            return Select(element).select_by_value(value)
        elif index:
            return Select(element).select_by_index(index)
        else:
            self.log.info("Element: " + element + "is NOT selected")
            return False
