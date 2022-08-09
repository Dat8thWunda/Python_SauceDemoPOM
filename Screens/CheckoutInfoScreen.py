import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInfoScreen:

    def __init__(self, driver):
        self.driver = driver

    labelCheckout_xpath = "//span[@class='title'][contains(.,'Checkout: Your Information')]"
    textboxFirstname_xpath = "//input[contains(@id,'first-name')]"
    textboxLastname_xpath = "//input[contains(@id,'last-name')]"
    textboxPostalCode_xpath = "//input[contains(@id,'postal-code')]"
    continueButton_xpath = "//input[contains(@id,'continue')]"

    def confirmCheckoutInformation(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.labelCheckout_xpath)))
        checkoutLabel = element.text

        if checkoutLabel == "CHECKOUT: YOUR INFORMATION":
            allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Information Page",
                          attachment_type=AttachmentType.PNG)
            print("Checkout page loaded. Enter your information")
            assert True
        else:
            print("Please reload the page")
            assert False

    def enterFirstname(self, Firstname):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textboxFirstname_xpath)))
        element.send_keys(Firstname)

    def enterLastname(self, Lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textboxLastname_xpath)))
        element.send_keys(Lastname)

    def enterPostalCode(self, PostalCode):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textboxPostalCode_xpath)))
        element.send_keys(PostalCode)

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.continueButton_xpath)))
        element.click()





