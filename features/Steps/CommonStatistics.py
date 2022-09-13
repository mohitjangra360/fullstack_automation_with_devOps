from behave import *

from Pages.CommonStatisticsPage import CommonStatisticsPage




@step("user is able to see Common statistics under dashboard")
def common_stats_displayed(context):
    common_stats_page = CommonStatisticsPage(context.driver)
    common_stats_page.common_stats_displayed()
