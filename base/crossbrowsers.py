import traceback
from selenium import webdriver
import os

class Browsers_setup():

    def __init__(self, browser):

        self.browser = browser
    """
     Set the PATH on the machine where browser will be executed
    """

    def cross_browsers(self):

        base_url = #ENTER URL""

        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "safari":
            serverLocation = "/Users/Julia/Desktop/webdriver/selenium-server-standalone-3.141.59.jar"
            os.environ["SELENIUM_SERVER_JAR"] = serverLocation
            driver = webdriver.Safari(quiet=True)
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.get(base_url)
        return driver