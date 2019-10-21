import utilities.logfile as logf
import logging
from base.basemethods import BaseMethods

class LoginPage(BaseMethods):

    log = logf.logfile(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[@href='/sign_in']"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "//input[@name='commit']"
    _avatar_logo= "//img[@class='gravatar']"
    _dropdown_menu= "//li[@class='dropdown open']//ul[@class='dropdown-menu']"
    _logout= "//a[contains(text(),'Log Out')]"


    def clickLoginLink(self):
        self.clickElement(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.getElement(self._email_field, locatorType="id").clear()
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.clickElement(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement(locator="search-courses", locatorType="id")
        result = self.isElementPresent("search-courses", locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyTitle("Let's Kode it")

    def clearemailfield(self):
        self.getElement(locator=self._email_field, locatorType="id").clear()

    def verifyLogOut(self):
        self.clickElement(locator=self._avatar_logo, locatorType="xpath")
        self.getElement(locator=self._dropdown_menu, locatorType="xpath")
        self.clickElement(locator=self._logout, locatorType="xpath")
        result = self.isElementPresent(locator="//a[@class='navbar-link fedora-navbar-link']",
                                       locatorType="xpath")
        return result