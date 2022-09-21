from behave import *

from Pages.Manufacture_Export import ManufactureExport


@step('I set search value as name "{}"')
def search_by_name(context, value):
    search = ManufactureExport(context.driver)
    search.search_by_name(value)


@step("I click on Search Button")
def step_impl(context):
    searchbtn = ManufactureExport(context.driver)
    searchbtn.i_click_on_search_btn()


@step('I see search result by name "{}"')
def step_impl(context, value):
    searchbtn = ManufactureExport(context.driver)
    searchbtn.i_see_search_result_by_name(value)
