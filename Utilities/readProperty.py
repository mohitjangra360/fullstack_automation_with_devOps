import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def goto_catalog_products():
        products = config.get('page url', 'catalog_products')
        return products
