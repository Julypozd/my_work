from base.custom_driver import CustomDriver
from traceback import print_stack
from utilities.utility import Utility


class BaseMethods(CustomDriver):

    def __init__(self, driver):

        super(BaseMethods, self).__init__(driver)
        self.driver = driver
        self.util = Utility()


    def verifyTitle(self, titleToVerify):

        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContain(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False