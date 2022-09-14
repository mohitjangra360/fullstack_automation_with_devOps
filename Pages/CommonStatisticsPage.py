from selenium.webdriver.common.by import By


class CommonStatisticsPage:
    # common_stats_By_xpath = "//div[@class='card-title' and normalize-space()='Common statistics']"
    # expand_collapse_btn_by_xpath = "//div[@class='card-header with-border clearfix' and normalize-space()='Common statistics']//button[@class='btn btn-tool']"

    def __init__(self, driver):
        self.driver = driver

    def common_stats_displayed(self, item):
        common_stats_By_xpath = f"//div[@class='card-title' and normalize-space()='{item}']"
        common_stats_status = self.driver.find_element(By.XPATH, common_stats_By_xpath).is_displayed()
        if common_stats_status:
            assert True
        else:
            assert False

    def expand_btn_display(self, btn):
        expand_collapse_btn_by_xpath = f"//div[@class='card-header with-border clearfix' and normalize-space()='{btn}']//button[@class='btn btn-tool']"
        expand_btn = self.driver.find_element(By.XPATH, expand_collapse_btn_by_xpath)
        expand_btn_status = expand_btn.is_displayed()
        if expand_btn_status:
            expand_btn.click()
        else:
            assert False

    def see_items_in_common_statistics(self):
        see_items_text_from_ui = self.driver.find_elements(By.XPATH,
                                                           "//div[@class='card-body']//div[@class='inner']//p")

        text_list = []

        for get_text_see_items in see_items_text_from_ui:
            list_of_items = get_text_see_items.text
            text_list.append(list_of_items)
        # print(text_list)
        remove_blank_value = list(filter(None, text_list))
        print(remove_blank_value)

    def collapse_btn_display_click(self, btn):
        expand_collapse_btn_by_xpath = f"//div[@class='card-header with-border clearfix' and normalize-space()='{btn}']//button[@class='btn btn-tool']"
        collapse_btn = self.driver.find_element(By.XPATH, expand_collapse_btn_by_xpath)
        collapse_btn_status = collapse_btn.is_displayed()
        if collapse_btn_status:
            collapse_btn.click()
        else:
            assert False
