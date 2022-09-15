from behave import *

from Pages.Manufacture_Export import ManufactureExport


@step("I should see export button")
def i_should_see_export_button(context):
    exp = ManufactureExport(context.driver)
    exp.i_should_see_export_button()

@step("I click on export button")
def i_click_on_export_button(context):
 exp_click = ManufactureExport(context.driver)
 exp_click.i_should_click_on_export_button()


@step("I should click on both dropdown list")
def i_should_click_on_both_dropdown_list(context):
    click_on_both = ManufactureExport(context.driver)
    click_on_both.i_should_click_on_both_dropdown_list()
