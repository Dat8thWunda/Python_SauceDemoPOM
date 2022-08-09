import pytest
from selenium import webdriver


@pytest.fixture()
def browser_setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver")
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="./Drivers/geckodriver")
        print("Launching Firefox browser")

    else:
        driver = webdriver.Edge(executable_path="./Drivers/msedgedriver")
        print("Launching MS Edge browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Sauce Demo Python POM'
#     config._metadata['Tester Name'] = 'Khilane'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('Java Home', None)
#     metadata.pop('Plugins', None)
