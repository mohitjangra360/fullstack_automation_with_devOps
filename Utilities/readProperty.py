import configparser

config = configparser.RawConfigParser()
TestDataSample = configparser.RawConfigParser()
SmsAppData = configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")
TestDataSample.read(".\\Test Data\\TestDataSample")
SmsAppData.read(".\\Test Data\\SmsAppData")

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

    # CREATED BY ADITYA
    @staticmethod
    def getDemoApplicationURL():
        demourl = config.get('Demo info', 'base_demoUrl')
        return demourl


    # CREATED BY ADITYA
    @staticmethod
    def getDemoUserName():
        demo_username = config.get('Demo info', 'Demo_username')
        return demo_username

    # CREATED BY ADITYA
    @staticmethod
    def getDemoPassword():
        demo_password = config.get('Demo info', 'Demo_password')
        return demo_password

    # CREATED BY ADITYA
    @staticmethod
    def getRecipientName():
        demo_recipientname = TestDataSample.get('Demo info', 'Recipient_name')
        return demo_recipientname

    # CREATED BY ADITYA
    @staticmethod
    def getRecipientEmail():
        demo_recipientEmail = TestDataSample.get('Demo info', 'Recipient_email')
        return demo_recipientEmail

    # CREATED BY ADITYA
    @staticmethod
    def getproducttitle():
        demo_producttitle = TestDataSample.get('Demo info', 'Product_Title')
        return demo_producttitle

    # CREATED BY ADITYA
    @staticmethod
    def getproductname():
        demo_productname = TestDataSample.get('Demo info', 'Product_Name')
        return demo_productname

    # CREATED BY ADITYA
    @staticmethod
    def getcheckouttitle():
        demo_checkouttitle = TestDataSample.get('Demo info', 'Checkout_Title')
        return demo_checkouttitle

    # CREATED BY ADITYA
    @staticmethod
    def getSMSApplicationURL():
        Appurl = config.get('App info', 'base_AppUrl')
        return Appurl

    # CREATED BY ADITYA
    @staticmethod
    def getSFUserName():
        SF_username = config.get('App info', 'App_username')
        return SF_username

    # CREATED BY ADITYA
    @staticmethod
    def getSFPassword():
        SF_password = config.get('App info', 'App_password')
        return SF_password

class AppData:

    @staticmethod
    def getrecordname():
        name = SmsAppData.get('Pre Conditions', 'Record_name')
        return name
    @staticmethod
    def getsenderphone():
        number = SmsAppData.get('Pre Conditions', 'Sender_phone')
        return number
    @staticmethod
    def getsendtoapi():
        api = SmsAppData.get('Pre Conditions', 'Send_to_api')
        return api
    @staticmethod
    def getchannel():
        channel = SmsAppData.get('Pre Conditions', 'Channel')
        return channel
    @staticmethod
    def getfolder():
        folder = SmsAppData.get('Pre Conditions', 'Folder')
        return folder
    @staticmethod
    def getdripcampaign():
        drip = SmsAppData.get('Pre Conditions', 'Drip Campaign')
        return drip
    @staticmethod
    def getsmstemplate():
        template = SmsAppData.get('Pre Conditions', 'SMS Template')
        return template