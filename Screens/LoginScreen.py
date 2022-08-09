import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.Custom_Logger import LogGen


class LoginScreen:
    textbox_username_xpath = "//input[contains(@id,'user-name')]"
    textbox_password_xpath = "//input[contains(@id,'password')]"
    button_submit_xpath = "//input[@type='submit']"
    label_loginFailed_xpath = "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match " \
                              "any user in this service')] "
    products_label_xpath = "//span[@class='title'][contains(.,'Products')]"

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_username_xpath)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_password_xpath)))
        element.send_keys(password)

    def clickSubmitButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_submit_xpath)))
        element.click()

    def verifyUnsuccessfulLogion(self):
        wait = WebDriverWait(self.driver, 30)
        loginError = wait.until(EC.element_to_be_clickable((By.XPATH, self.label_loginFailed_xpath))).text

        if loginError == "Epic sadface: Username and password do not match any user in this service":
            allure.attach(self.driver.get_screenshot_as_png(), name="Unsuccessful Login",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("******  Invalid login test has passed ******")
            self.driver.quit()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed Test Screenshot",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("******  Invalid login test has failed ******")
            self.driver.quit()
            assert False

    def verifySuccessfulLogin(self):

        successLogin = self.driver.find_element(By.XPATH, self.products_label_xpath).text

        if successLogin == "PRODUCTS":
            allure.attach(self.driver.get_screenshot_as_png(), name="Successful Login",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("******  Successful login test has passed ******")
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed `Successful Test",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("******  Successful login test has failed ******")
            self.driver.quit()
            assert False
