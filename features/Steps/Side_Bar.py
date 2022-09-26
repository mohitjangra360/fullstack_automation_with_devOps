from behave import *

from Pages.Side_Bar_Page import SideBarPage


@step("I should see logo")
def i_should_see_logo(context):
    logo = SideBarPage(context.driver)
    logo.i_should_see_logo()


@step("I should see search box")
def i_should_see_search_box(context):
   search_box = SideBarPage(context.driver)
   search_box.i_should_see_search_box()


@step("I should see all side menu item is visible and clickable")
def check_side_menu_item_is_visible_clickable(context):
    side_bar_item = SideBarPage(context.driver)
    side_bar_item.i_should_see_side_bar_item_is_visible_and_clickable()