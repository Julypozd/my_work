import utilities.logfile as logf
import logging
from base.custom_driver import CustomDriver
from traceback import print_stack

class TestStatus(CustomDriver):

    log = logf.logfile(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def markResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL ###" + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED ###" + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED ###" + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred ###")
            self.screenShot(resultMessage)
            print_stack()

    def markPoint(self, result, resultMessage):
        self.markResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        # final test status of the test case
        self.markResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName +" ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True

