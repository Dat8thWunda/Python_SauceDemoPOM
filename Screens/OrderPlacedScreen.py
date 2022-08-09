import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPlacedScreen:

    def __init__(self, driver):
        self.driver = driver

    checkoutCompletepage_xpath = "//span[@class='title'][contains(.,'Checkout: Complete!')]"
    checkoutComplete_xpath = "//div[@class='complete-text'][contains(.,'Your order has been dispatched, and will arrive just as fast as the pony can get there!')] "

    cancelButton_xpath = "//button[contains(@id,'cancel')]"
    openMenubutton_xpath = "//button[contains(@id,'react-burger-menu-btn')]"
    logoutButton_xpath = "//a[contains(.,'Logout')]"

    def completeCheckout(self):
        wait = WebDriverWait(self.driver, 15)
        checkoutComplete = wait.until(EC.element_to_be_clickable((By.XPATH, self.checkoutComplete_xpath))).text
        checkoutCompletePage = wait.until(EC.element_to_be_clickable((By.XPATH, self.checkoutCompletepage_xpath))).text

        if checkoutComplete == "Your order has been dispatched, and will arrive just as fast as the pony can get there!" and checkoutCompletePage == "CHECKOUT: COMPLETE!":
            allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Complete!",
                          attachment_type=AttachmentType.PNG)
            print("Your order has been successfully placed. Please come again soon!")
            self.driver.quit()
            assert True
        else:
            print("Your order has not been successfully placed. Please try again soon!")
            wait = WebDriverWait(self.driver, 15)
            cancel = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancelButton_xpath)))
            cancel.click()
            openMenu = wait.until(EC.element_to_be_clickable((By.XPATH, self.openMenubutton_xpath)))
            openMenu.click()
            logoutButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath)))
            logoutButton.click()



