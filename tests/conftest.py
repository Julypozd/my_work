import pytest
from base.crossbrowsers import BrowsersSetup
#from pages.home.loginpage import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    brw = BrowsersSetup(browser)
    driver = brw.CrossBrowsers()
    #lp = LoginPage(driver)
    #lp.login(email="test@email.com", password="abcabc")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--OStype", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--OStype")