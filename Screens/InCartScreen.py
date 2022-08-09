import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class InCartScreen:

    def __init__(self, driver):
        self.driver = driver

    Cart_xpath = "//a[contains(@class,'shopping_cart_link')]"
    InCartItem_xpath = "//div[@class='inventory_item_name'][contains(.,'Test.allTheThings() T-Shirt (Red)')]"
    checkoutButton_xpath = "//button[contains(@id,'checkout')]"

    def enterTheCart(self):
        time.sleep(1)
        enterCart = self.driver.find_element(By.XPATH, self.Cart_xpath)
        enterCart.click()

    def checkItemInCart(self):
        time.sleep(1)
        CartItem = self.driver.find_element(By.XPATH, self.InCartItem_xpath)

        if CartItem.is_displayed():
            print("Item is found in basket")
            allure.attach(self.driver.get_screenshot_as_png(), name="Item is located in the cart.",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            print("Item not found in basket")
            self.driver.quit()
            assert False

    def checkoutButton(self):
        time.sleep(1)
        CheckoutButton = self.driver.find_element(By.XPATH, self.checkoutButton_xpath)
        CheckoutButton.click()

