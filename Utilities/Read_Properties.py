import configparser

config = configparser.RawConfigParser()
config.read("/Users/saneleg/PycharmProjects/Sauce_Demo_POM/Configurations_Setup/config.ini")


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        BaseURL = config.get('Common Details', 'BaseURL')
        return BaseURL

    @staticmethod
    def getUsername():
        Username = config.get('Login Details', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('Login Details', 'Password')
        return Password

    @staticmethod
    def getFirstname():
        FirstName = config.get('Checkout Details', 'Firstname')
        return FirstName

    @staticmethod
    def getLastname():
        Lastname = config.get('Checkout Details', 'Lastname')
        return Lastname

    @staticmethod
    def getPostalcode():
        PostalCode = config.get('Checkout Details', 'Postalcode')
        return PostalCode
