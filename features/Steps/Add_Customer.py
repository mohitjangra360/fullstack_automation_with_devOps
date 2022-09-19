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


@step("I click on add new button")
def click_on_add_new_cust_btn(context):
    a = Add_Customer(context.driver)
    a.click_on_add_new_cust_btn()


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


@step('I select gender as "{}"')
def set_gender(context, gender):
     a = Add_Customer(context.driver)
     a.set_gender(gender)


@step('I set dob as "{}"')
def set_dob(context, dob):
    a = Add_Customer(context.driver)
    a.set_dob(dob)


@step('I set customer role as "{}"')
def set_customer_role(context, role):
    a = Add_Customer(context.driver)
    a.set_customer_role(role)

