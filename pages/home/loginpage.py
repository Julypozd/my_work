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
    _avatar_logo = "//img[@class='gravatar']"
    _dropdown_menu = "//li[@class='dropdown open']//ul[@class='dropdown-menu']"
    _logout = "//a[contains(text(),'Log Out')]"

    def click_login_link(self):
        self.click_element(self._login_link, locator_type="xpath")

    def enter_email(self, email):
        self.get_element(self._email_field, locator_type="id").clear()
        self.send_keys(email, self._email_field, locator_type="id")

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.click_element(self._login_button, locator_type="xpath")

    def login(self, email="", password=""):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        self.wait_for_element(locator="search-courses", locator_type="id")
        result = self.is_element_present("search-courses", locator_type="id")
        return result

    def verify_login_failed(self):
        result = self.is_element_present("//div[contains(text(),'Invalid email or password')]",
                                         locator_type="xpath")
        return result

    def verify_login_title(self):
        return self.verify_title("Let's Kode it")

    def clear_email_field(self):
        self.get_element(locator=self._email_field, locator_type="id").clear()

    def verify_log_out(self):
        self.click_element(locator=self._avatar_logo, locator_type="xpath")
        self.get_element(locator=self._dropdown_menu, locator_type="xpath")
        self.click_element(locator=self._logout, locator_type="xpath")
        result = self.is_element_present(locator="//a[@class='navbar-link fedora-navbar-link']",
                                         locator_type="xpath")
        return result
