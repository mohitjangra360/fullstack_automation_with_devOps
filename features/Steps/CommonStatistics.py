from behave import *

from Pages.CommonStatisticsPage import CommonStatisticsPage


@step('user is able to see "{}" under dashboard')
def common_stats_displayed(context, item):
    select_item = CommonStatisticsPage(context.driver)
    select_item.common_stats_displayed(item)


@step('Verify user must be able to see Expand button for "{}" is visible')
def see_expand_btn(context, btn):
    see_expand = CommonStatisticsPage(context.driver)
    see_expand.expand_btn_display(btn)


@step('Click on expand icon of "{}"')
def click_on_expand_btn(context, btn):
    click_on_expand = CommonStatisticsPage(context.driver)
    click_on_expand.expand_btn_display(btn)


@step("Verify user is able to see items in common statistics")
def see_items_common_statistics(context):
    see_items = CommonStatisticsPage(context.driver)
    see_items.see_items_in_common_statistics()


@step('Click on collapse icon of "{}"')
def click_on_collapse_btn(context, btn):
    collapse_btn = CommonStatisticsPage(context.driver)
    collapse_btn.collapse_btn_display_click(btn)
