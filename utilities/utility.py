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

    def get_alpha_numeric(self, length, type='letters'):

        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have.
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

    def get_unique_name(self, char_count=10):
        """
        Get a unique name
        """
        return self.get_alpha_numeric(char_count, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of valid email ids

        Parameters:
            list_size: Number of names. Default is 5 names in a list
            item_length: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contain(self, actual_text, expected_text):

        self.mylog.info("Actual text is:" + actual_text)
        self.mylog.info("Expected text is:" + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.mylog.info("Verification Successful")
            return True
        else:
            self.mylog.info("Verification FAILED with this text" + actual_text)
            return False

    def verify_text_match(self, actual_text, expected_text):

        self.mylog.info("Actual text is" + actual_text)
        self.mylog.info("Expected text is " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.mylog.info("Verification Successful")
            return True
        else:
            self.mylog.info("Verification FAILED with this text" + actual_text)
            return False

    def verify_list_match(self, expected_list, actual_list):

        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):

        length = len(expected_list)
        for x in range(0, length):
            if expected_list[x] not in actual_list:
                return False
        else:
            return True