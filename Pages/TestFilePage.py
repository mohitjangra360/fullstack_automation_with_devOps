import time
from telnetlib import EC
from selenium.webdriver.common.by import By


class TestFilePage:
    logo_by_xpath = "//img[@class='brand-image-xl logo-xl']"
    searchbox_by_id = "search-box"

    def __init__(self, driver):
        self.driver = driver

    def i_should_see_logo(self):
        logo = self.driver.find_element(By.XPATH, self.logo_by_xpath).is_displayed()
        if logo == True:
            assert True
        else:
            assert False

    def i_should_see_search_box(self):
        searchbox = self.driver.find_element(By.ID, self.searchbox_by_id).is_displayed()
        if searchbox == True:
            assert True
        else:
            assert False

    def i_should_see_all_side_menu_item_is_visible(self):
        menuitem = "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' ]//p"
        getValue = self.driver.find_elements(By.XPATH, menuitem)
        listitem = []
        for all_item in getValue:
            item_text = all_item.text
            listitem.append(item_text)
        print(listitem)
        remove_blank_value = list(filter(None, listitem))
        print(remove_blank_value)
        for index_click in remove_blank_value:
            item_click_by_xpath = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(), '{index_click}')]"
            self.driver.find_element(By.XPATH, item_click_by_xpath).click()
            time.sleep(2)




