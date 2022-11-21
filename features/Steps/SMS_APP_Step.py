import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Sms_App_Page import SMSAPP_Demo
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig, AppData

baseAppUrl = ReadConfig.getSMSApplicationURL()
mylog = LogGen.loggen()
username = ReadConfig.getSFUserName()
password = ReadConfig.getSFPassword()
record = AppData.getrecordname()
s_number = AppData.getsenderphone()
m_type = AppData.getchannel()
f_type = AppData.getfolder()
d_type = AppData.getdripcampaign()
t_type = AppData.getsmstemplate()

@step("Open Browser and salesforce")
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    mylog.info("Open Browser")
    context.driver.get(baseAppUrl)

@step("I am On Salesforce Login Page")
def user_on_login_page(context):
    global logopage
    actual_title = context.driver.title
    expected_title = "Login | Salesforce"
    if actual_title == expected_title:
        assert True
    else:
        assert False

@step("I Login")
def user_login_as_admin(context):
    common_method = SMSAPP_Demo(context.driver)
    common_method.setSFUsername(username)
    common_method.setSFPassword(password)
    common_method.clickOnSFLogin_btn()

@step("Verify user must be on classic page.")
def verify_user_must_on_classic_page(context):
    classic = SMSAPP_Demo(context.driver)
    classic.classicpage()

@step('Verify user must be on "{}" App layout.')
def verify_user_must_be_on_App_layout(context, menu):
    click_btn = SMSAPP_Demo(context.driver)
    click_btn.Verify_user_on_App_layout(menu)

@step('Click on "{}" object')
def Click_on_object(context, object):
    click_obj = SMSAPP_Demo(context.driver)
    click_obj.click_object(object)

@step('Verify "{}" selected and Click GO')
def Click_Go(context, select):
    click_go = SMSAPP_Demo(context.driver)
    click_go.click_go_and_verify_selected(select)

@step("Click record from list")
def Select_any_record_from_list(context):
    click_record = SMSAPP_Demo(context.driver)
    click_record.click_any_object_record(record)

@step("Click send sms button on record page")
def Click_sendsms_button_on_record_page(context):
    click_sendsms = SMSAPP_Demo(context.driver)
    click_sendsms.click_sendsms_button()

@step("Verify Send SMS page details")
def Click_sendsms_button_on_record_page(context):
    verify_page = SMSAPP_Demo(context.driver)
    verify_page.verify_sendsms_pagedetails(s_number, m_type, f_type, d_type, t_type)

@step("Write Text in textbox field and click send")
def Click_sendsms_button_on_record_page(context):
    click_sendsms = SMSAPP_Demo(context.driver)
    click_sendsms.click_send_button_on_detailpage(record)

@step('Click on "{}" object and Click Go and verify "{}" selected')
def Verify_outgoing_history(context, object, select):
    verify_history = SMSAPP_Demo(context.driver)
    verify_history.click_object(object)
    verify_history.click_go_and_verify_selected(select)
    verify_history.verify_outgoing_history()