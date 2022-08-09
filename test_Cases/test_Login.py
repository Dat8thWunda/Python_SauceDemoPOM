import allure
import pytest

from Screens.CheckoutInfoScreen import CheckoutInfoScreen
from Screens.CheckoutOverviewScreen import CheckoutOverviewScreen
from Screens.HomeScreen import HomeScreen
from Screens.InCartScreen import InCartScreen
from Screens.LoginScreen import LoginScreen
from Screens.OrderPlacedScreen import OrderPlacedScreen
from Utilities.Custom_Logger import LogGen
from Utilities.Read_Properties import ReadConfig


@allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    BaseURL = ReadConfig.getBaseUrl()
    Username = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()

    Firstname = ReadConfig.getFirstname()
    Lastname = ReadConfig.getLastname()
    PostalCode = ReadConfig.getPostalcode()

    logger = LogGen.loggen()

    # Test Invalid log in details
    @pytest.mark.test
    @allure.severity(allure.severity_level.CRITICAL)
    def test_InvalidLogin(self, browser_setup) -> None:
        self.driver = browser_setup
        self.logger.info("****** Invalid login test has started ******")
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.LS = LoginScreen(self.driver)
        self.LS.enterUsername(self.Username + "Invalid")
        self.LS.enterPassword(self.Password)
        self.LS.clickSubmitButton()
        self.LS.verifyUnsuccessfulLogion()
        self.logger.info("******  Invalid login has ended ******")

    # Test Valid log in details
    @pytest.mark.test
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ValidLogin(self, browser_setup) -> None:
        self.driver = browser_setup
        self.logger.info("****** Valid login test has started ******")
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.LS = LoginScreen(self.driver)
        self.LS.enterUsername(self.Username)
        self.LS.enterPassword(self.Password)
        self.LS.clickSubmitButton()
        self.LS.verifySuccessfulLogin()
        self.logger.info("******  Valid login has ended ******")

        # Verify homepage and add item to cart
        self.logger.info("****** Add to cart test has started ******")
        self.HS = HomeScreen(self.driver)
        self.HS.ConfirmHomePage()
        self.HS.AddItemtoCart()
        self.HS.VerifyItemAddedtoCart()
        self.logger.info("****** Add to cart has ended ******")

        # Check the contents of the cart and verify that the item is added
        self.logger.info("****** Cart contents check test has started ******")
        self.ICS = InCartScreen(self.driver)
        self.ICS.enterTheCart()
        self.ICS.checkItemInCart()
        self.ICS.checkoutButton()
        self.logger.info("****** Cart contents check has ended ******")

        # Verify the checkout information screen and enter the information required
        self.logger.info("****** Checkout info page test has started ******")
        self.CIS = CheckoutInfoScreen(self.driver)
        self.CIS.confirmCheckoutInformation()
        self.CIS.enterFirstname(self.Firstname)
        self.CIS.enterLastname(self.Lastname)
        self.CIS.enterPostalCode(self.PostalCode)
        self.CIS.clickContinueButton()
        self.logger.info("****** Checkout info page test has ended ******")

        # Check if the item added is in the final basket and also confirm the prices
        self.logger.info("****** Checkout Overview page test has started ******")
        self.COS = CheckoutOverviewScreen(self.driver)
        self.COS.confirmCheckoutOverview()
        self.COS.confirmItemPrices()
        self.COS.clickFinishbutton()
        self.logger.info("****** Checkout Overview  page test has ended ******")

        # Confirm that the order has been placed successfully and shut down the browser
        self.logger.info("****** Order placed page test has started ******")
        self.OPS = OrderPlacedScreen(self.driver)
        self.OPS.completeCheckout()
        self.logger.info("****** Order placed page test has ended ******")
