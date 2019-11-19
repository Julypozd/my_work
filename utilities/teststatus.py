import utilities.logfile as logf
import logging
from base.custom_driver import Custom_driver
from traceback import print_stack

class TestStatus(Custom_driver):

    log = logf.logfile(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def mark_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL ###" + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED ###" + result_message)
                    self.screen_shot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED ###" + result_message)
                self.screen_shot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception Occurred ###")
            self.screen_shot(result_message)
            print_stack()

    def mark_point(self, result, result_message):
        self.mark_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        # final test status of the test case
        self.mark_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True

