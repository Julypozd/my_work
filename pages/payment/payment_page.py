import utilities.logfile as logf
import logging
from base.basemethods import BaseMethods
from selenium.webdriver.support.ui import Select

class Payment_page(BaseMethods):

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
        self.sendKeys(name, self._search_field, locatorType="id")
        self.clickElement(self._search_button, locatorType="id")

    def select_course_topay(self):
        self.clickElement(locator=self._course_name, locatorType="xpath")

    def click_enroll(self):
        self.clickElement(self._enroll_button)

    def select_visa_method(self):
        self.clickElement(locator=self._payment_method, locatorType="xpath")
        self.getElement(locator=self._all_pay_methods, locatorType="id")
        self.clickElement(locator=self._visa_, locatorType="xpath")

    def select_paypal_method(self):
        self.clickElement(locator=self._payment_method, locatorType="xpath")
        self.getElement(locator=self._all_pay_methods, locatorType="id")
        self.clickElement(locator=self._pay_pal_, locatorType="xpath")

    def enter_card_num(self, cardnumber):
        self.switchToFrame(name="__privateStripeFrame8")
        self.sendKeys(cardnumber, locator=self._cc_num, locatorType='xpath')
        self.switchToDefaultContent()

    def enter_expdate(self, expdate):
        self.switchToFrame(name="__privateStripeFrame9")
        self.sendKeys(expdate, locator=self._cc_exp, locatorType='name' )
        self.switchToDefaultContent()

    def enter_cvc(self, cvc):
        self.switchToFrame(name="__privateStripeFrame10")
        self.sendKeys(cvc, locator=self._cc_cvc, locatorType='name' )
        self.switchToDefaultContent()

    def enter_zip(self, zip):
        self.switchToFrame(name="__privateStripeFrame11")
        self.sendKeys(zip, locator=self._zip_, locatorType="name")
        self.switchToDefaultContent()

    def click_agreeterms(self):
        self.clickElement(locator=self._agree_toterms)

    def click_EnrollSubmit(self):
        self.clickElement(locator=self._submit_enroll, locatorType="xpath")

    def enter_visa_payment(self, cardnumber, expdate, cvc, zip):
        self.select_visa_method()
        self.enter_card_num(cardnumber)
        self.enter_expdate(expdate)
        self.enter_cvc(cvc)
        self.enter_zip(zip)

    def enter_paypal_payment(self):
        self.select_paypal_method()
        self.clickElement(locator="country_code_credit_card-paypal", locatorType="id")
        element= self.getElement(locator="country_code_credit_card-paypal", locatorType="id")
        sel= Select(element)
        sel.select_by_visible_text("Algeria")
        self.clickElement(locator=self._agree_toterms, locatorType="id")

    def enroll_java_visa(self, cardnum="", expdate="", cvc="", zip=""):
        self.click_enroll()
        self.scrollPage(direction="down")
        self.select_visa_method()
        self.enter_visa_payment(cardnum, expdate, cvc, zip)
        self.click_agreeterms()

    def enroll_java_paypal(self):
        self.click_enroll()
        self.scrollPage(direction="down")
        self.select_paypal_method()
        self.enter_paypal_payment()
        self.click_agreeterms()

    def verifyEnrollFailed(self):
        result1= self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Submit payment visa")
        return result1

    def paypalPass(self):
        resultPP= self.isEnabled(locator=self._paypal_enroll, info="Submit paypal payment")
        return resultPP









