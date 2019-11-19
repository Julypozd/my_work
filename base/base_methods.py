from base.custom_driver import Custom_driver
from traceback import print_stack
from utilities.utility import Utility


class Base_methods(Custom_driver):

    def __init__(self, driver):

        super(Base_methods, self).__init__(driver)
        self.driver = driver
        self.util = Utility()


    def verifyTitle(self, title_to_verify):

        try:
            actual_title = self.get_title()
            return self.util.verify_text_contain(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False