import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class HomeScreen:

    button_open_menu = "//button[contains(.,'Open Menu')]"
    logout_sidebar_option = "//a[contains(@id,'logout_sidebar_link')]"
    button_close_menu = "//button[contains(.,'Close Menu')]"
    chosen_item_xpath = "//button[contains(@id,'add-to-cart-test.allthethings()-t-shirt-(red)')]"
    item_in_cart_xpath = "//div[@class='inventory_item_name'][contains(.,'Test.allTheThings() T-Shirt (Red)')]"

    def __init__(self, driver):
        self.driver = driver

    def ConfirmHomePage(self):

        time.sleep(1)
        openMenu = self.driver.find_element(By.XPATH, self.button_open_menu)
        openMenu.click()

        time.sleep(1)
        LogoutOption = self.driver.find_element(By.XPATH, self.logout_sidebar_option)
        if LogoutOption.is_displayed():
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name="Logout Menu successfully displayed",
                          attachment_type=AttachmentType.PNG)
            print("Logout menu successfully loaded")
            self.driver.find_element(By.XPATH, self.button_close_menu).click()
            assert True
        else:
            print("Logout menu failed to load")
            self.driver.find_element(By.XPATH, self.button_close_menu).click()
            assert False

    def AddItemtoCart(self):
        time.sleep(1)
        AdditemtoCart = self.driver.find_element(By.XPATH, self.chosen_item_xpath)
        AdditemtoCart.click()

    def VerifyItemAddedtoCart(self):
        time.sleep(1)
        ItemInCart = self.driver.find_element(By.XPATH, self.item_in_cart_xpath)
        if ItemInCart.is_displayed():
            allure.attach(self.driver.get_screenshot_as_png(), name="Item added to cart Successfully",
                          attachment_type=AttachmentType.PNG)
            print("Item was added to cart")
            assert True
        else:
            print("Item was not added to cart")
            assert False







