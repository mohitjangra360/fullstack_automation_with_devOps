import random
import string

from behave import *

from Pages.Add_Customer_Page import Add_Customer


@step("I click on Customers")
def click_on_customer_item(context):
    a = Add_Customer(context.driver)
    a.click_on_customer_item()


@step("I select Customer under Customer Menu Item")
def click_on_menu_link_item_for_cust(context):
    a = Add_Customer(context.driver)
    a.click_on_menu_link_item_for_cust()

@step("I verify add new button")
def verify_add_new_cust_btn(context):
    a = Add_Customer(context.driver)
    a.Verify_add_new_cust_btn_on_Page()

@step("I click on add new button")
def click_on_add_new_cust_btn(context):
    a = Add_Customer(context.driver)
    a.click_on_add_new_cust_btn()

@step('I verify page title "{}"')
def click_on_add_new_cust_btn(context, title):
    a = Add_Customer(context.driver)
    a.verify_create_page_title(title)

@step("I set Email")
def set_mail_for_cust(context):
    a = Add_Customer(context.driver)
    a.set_mail_for_cust()


@step('I set Password "{}"')
def set_password(context, password):
     a = Add_Customer(context.driver)
     a.set_password(password)


@step('I set First name as "{}"')
def set_firstname(context, firstname):
      a = Add_Customer(context.driver)
      a.set_firstname(firstname)


@step('I set Last name as "{}"')
def set_lastname(context, lastname):
     a = Add_Customer(context.driver)
     a.set_lastname(lastname)


@step('I select gender as "{Male}"')
def set_gender(context, gender):
     a = Add_Customer(context.driver)
     a.set_gende(set_gender)