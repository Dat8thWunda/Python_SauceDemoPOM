import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewScreen:

    def __init__(self, driver):
        self.driver = driver

    labelCheckoutOverview_xpath = "//span[@class='title'][contains(.,'Checkout: Overview')]"
    itemPurchased_xpath = "//div[@class='inventory_item_name'][contains(.,'Test.allTheThings() T-Shirt (Red)')]"

    cancelButton_xpath = "//button[contains(@id,'cancel')]"
    openMenubutton_xpath = "//button[contains(@id,'react-burger-menu-btn')]"
    logoutButton_xpath = "//a[contains(.,'Logout')]"

    finishButton_xpath = "//button[contains(@id,'finish')]"

    itemTotal_xpath = "//div[@class='summary_subtotal_label'][contains(.,'')]"
    taxTotal_xpath = "//div[@class='summary_tax_label'][contains(.,'')]"
    total_xpath = "//div[@class='summary_total_label'][contains(.,'')]"

    def confirmCheckoutOverview(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.labelCheckoutOverview_xpath)))
        CheckoutLabel = element.text

        if CheckoutLabel == "CHECKOUT: OVERVIEW":
            allure.attach(self.driver.get_screenshot_as_png(), name="Overview Page loaded",
                          attachment_type=AttachmentType.PNG)
            print("Checkout Overview page loaded. Confirm your billing.")
            assert True
        else:
            print("Please reload the page")
            assert False

    def confirmItemPrices(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.itemTotal_xpath)))
        ItemTotal = element.text
        Item = ItemTotal[13:18]

        Element = wait.until(EC.element_to_be_clickable((By.XPATH, self.taxTotal_xpath)))
        TaxTotal = Element.text
        Tax = TaxTotal[6:10]

        elements = wait.until(EC.element_to_be_clickable((By.XPATH, self.total_xpath)))
        Total = elements.text
        Tot = Total[8:13]

        Final = float(Item) + float(Tax)
        if Final == float(Tot):
            print(Item)
            print(Tax)
            print(Tot)
            print("Total is correct")
            assert True
        else:
            print("Incorrect total")
            wait = WebDriverWait(self.driver, 15)
            cancel = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancelButton_xpath)))
            cancel.click()
            openMenu = wait.until(EC.element_to_be_clickable((By.XPATH, self.openMenubutton_xpath)))
            openMenu.click()
            logoutButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath)))
            logoutButton.click()
            self.driver.quit()
            assert False

    def clickFinishbutton(self):
        wait = WebDriverWait(self.driver, 15)
        finishButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.finishButton_xpath)))
        finishButton.click()
