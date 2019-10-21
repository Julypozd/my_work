import time
import traceback
import random, string
import utilities.logfile as log
import logging

class Utility(object):

    mylog = log.logfile(logging.INFO)

    def sleep(self, sec, info=""):

        if info is not None:
            self.mylog.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Parameters:
            listSize: Number of names. Default is 5 names in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContain(self, actualText, expectedText):

        self.mylog.info("Actual text is:" + actualText)
        self.mylog.info("Expected text is:" + expectedText)
        if expectedText.lower() in actualText.lower():
            self.mylog.info("Verification Successful")
            return True
        else:
            self.mylog.info("Verification FAILED with this text" + actualText)
            return False

    def verifyTextMatch(self, actualText, expectedText):

        self.mylog.info("Actual text is" + actualText)
        self.mylog.info("Expected text is " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.mylog.info("Verification Successful")
            return True
        else:
            self.mylog.info("Verification FAILED with this text" + actualText)
            return False

    def verifyListMatch(self, expectedList, actualList):

        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):

        length = len(expectedList)
        for x in range(0, length):
            if expectedList[x] not in actualList:
                return False
        else:
            return True