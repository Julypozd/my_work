from selenium import webdriver
import os


class BrowsersSetup():

    def __init__(self, browser):

        self.browser = browser
    """
     Set the PATH on the machine where browser will be executed
    """

    def cross_browsers(self):

        base_url = "................"

        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "safari":
            server_location = "/Users/Julia/Desktop/webdriver/selenium-server-standalone-3.141.59.jar"
            os.environ["SELENIUM_SERVER_JAR"] = server_location
            driver = webdriver.Safari(quiet=True)
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.get(base_url)
        return driver
