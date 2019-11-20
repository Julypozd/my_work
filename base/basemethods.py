from base.customdriver import CustomDriver
from traceback import print_stack
from utilities.utility import Utility


class BaseMethods(CustomDriver):

    def __init__(self, driver):

        super(BaseMethods, self).__init__(driver)
        self.driver = driver
        self.util = Utility()

    def verify_title(self, title_to_verify):

        try:
            actual_title = self.get_title()
            return self.util.verify_text_contain(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
