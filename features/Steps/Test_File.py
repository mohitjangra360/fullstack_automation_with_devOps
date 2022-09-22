from behave import *

from Pages.TestFilePage import TestFilePage


#@step("I should see logo")
#def i_should_see_log0(context):
 #   logo = TestFilePage(context.driver)
  #  logo.i_should_see_logo()


#@step("I should see search box")
#def i_should_see_search_box(context):
 #   search_box = TestFilePage(context.driver)
  #  search_box.i_should_see_search_box()


@step("I should see all side menu item is visible")
def i_should_see_all_side_menu_item_is_visible(context):
    menu_item = TestFilePage(context.driver)
    menu_item.i_should_see_all_side_menu_item_is_visible()