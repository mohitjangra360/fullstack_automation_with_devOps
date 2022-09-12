from behave import *

from Pages.Searchbar import Search

@step("User should see Searchbar")
def user_should_see_searchbar(context):
    SB = Search(context.driver)
    SB.user_should_see_searchbar()

@step("User able to click in Search bar")
def user_should_click_searchbar(context):
    """
    :type context: behave.runner.Context
    """
    SB_click = Search(context.driver)
    SB_click.user_should_click_searchbar()