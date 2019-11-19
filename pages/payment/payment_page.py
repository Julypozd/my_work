import utilities.logfile as logf
import logging
from base.base_methods import Base_methods
from selenium.webdriver.support.ui import Select

class Payment_page(Base_methods):

    log = logf.logfile(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_field = "search-payment"
    _search_button= "search-course-button"
    _course_name = "//div[contains(text(),'JavaScript for beginners')]" #JavaScript for beginners
    _all_courses = "//div[@class='course-listing-title']"
    _enroll_button="enroll-button-top"
    _payment_method = "//button[@class='dropbtn minimal']"
    _all_pay_methods= "option-container"
    _visa_= "//div[@id='option-container']//a[1]"
    _pay_pal_= "//div[@id='option-container']//a[2]"
    #iframes
    _cc_num= "//input[@aria-label='Credit or debit card number']" #iframe8
    _cc_exp= 'exp-date' #name #irame9
    _cc_cvc= 'cvc' #name iframe10
    _zip_= 'postal' #name iframe11

    _agree_toterms='agreed_to_terms_checkbox'
    _submit_enroll= "//div[@class='spc__primary-submit']"
    _paypal_enroll= "confirm-purchase"

    def enter_course_name(self, name):
        self.send_keys(name, self._search_field, locator_type="id")
        self.click_element(self._search_button, locator_type="id")

    def select_course_topay(self):
        self.click_element(locator=self._course_name, locator_type="xpath")

    def click_enroll(self):
        self.click_element(self._enroll_button)

    def select_visa_method(self):
        self.click_element(locator=self._payment_method, locator_type="xpath")
        self.get_element(locator=self._all_pay_methods, locator_type="id")
        self.click_element(locator=self._visa_, locator_type="xpath")

    def select_paypal_method(self):
        self.click_element(locator=self._payment_method, locator_type="xpath")
        self.get_element(locator=self._all_pay_methods, locator_type="id")
        self.click_element(locator=self._pay_pal_, locator_type="xpath")

    def enter_card_num(self, cardnumber):
        self.switch_to_frame(name="__privateStripeFrame8")
        self.send_keys(cardnumber, locator=self._cc_num, locator_type='xpath')
        self.switch_to_default_content()

    def enter_expdate(self, expdate):
        self.switch_to_frame(name="__privateStripeFrame9")
        self.send_keys(expdate, locator=self._cc_exp, locator_type='name')
        self.switch_to_default_content()

    def enter_cvc(self, cvc):
        self.switch_to_frame(name="__privateStripeFrame10")
        self.send_keys(cvc, locator=self._cc_cvc, locator_type='name')
        self.switch_to_default_content()

    def enter_zip(self, zip):
        self.switch_to_frame(name="__privateStripeFrame11")
        self.send_keys(zip, locator=self._zip_, locator_type="name")
        self.switch_to_default_content()

    def click_agreeterms(self):
        self.click_element(locator=self._agree_toterms)

    def click_enroll_submit(self):
        self.click_element(locator=self._submit_enroll, locator_type="xpath")

    def enter_visa_payment(self, cardnumber, expdate, cvc, zip):
        self.select_visa_method()
        self.enter_card_num(cardnumber)
        self.enter_expdate(expdate)
        self.enter_cvc(cvc)
        self.enter_zip(zip)

    def enter_paypal_payment(self):
        self.select_paypal_method()
        self.click_element(locator="country_code_credit_card-paypal", locator_type="id")
        element= self.get_element(locator="country_code_credit_card-paypal", locator_type="id")
        sel= Select(element)
        sel.select_by_visible_text("Algeria")
        self.click_element(locator=self._agree_toterms, locator_type="id")

    def enroll_java_visa(self, cardnum="", expdate="", cvc="", zip=""):
        self.click_enroll()
        self.scroll_page(direction="down")
        self.select_visa_method()
        self.enter_visa_payment(cardnum, expdate, cvc, zip)
        self.click_agreeterms()

    def enroll_java_paypal(self):
        self.click_enroll()
        self.scroll_page(direction="down")
        self.select_paypal_method()
        self.enter_paypal_payment()
        self.click_agreeterms()

    def verify_enroll_failed(self):
        result1= self.is_enabled(locator=self._submit_enroll, locator_type="xpath",
                                 info="Submit payment visa")
        return result1

    def paypal_pass(self):
        result_pp= self.is_enabled(locator=self._paypal_enroll, info="Submit paypal payment")
        return result_pp









