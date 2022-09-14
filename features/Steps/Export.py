from behave import *

from Pages.Catalog.Export import Export


@step("User should see export")
def user_should_see_export(context):
    expo = Export(context.driver)
    expo.user_should_see_export()

@step("User able to click in export")
def user_should_click_export(context):
    expo_click = Export(context.driver)
    expo_click.user_should_click_export()
