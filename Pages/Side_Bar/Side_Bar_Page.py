import time
from telnetlib import EC
from selenium.webdriver.common.by import By


class SideBarPage:
    logo_by_xpath = "//img[@class='brand-image-xl logo-xl']"

    def __init__(self, driver):
        self.driver = driver

    def i_should_see_logo(self):
        logo = self.driver.find_element(By.XPATH, self.logo_by_xpath).is_displayed()
        if logo == True:
            assert True
        else:
            assert False

    def i_should_see_search_box(self):
        search_box = self.driver.find_element(By.ID, "search-box").is_displayed()
        if search_box == True:
            assert True
        else:
            assert False

    def i_should_see_side_bar_item_is_visible_and_clickable(self):
        main_heading_xpath = "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p"
        main_heading_xpath = self.driver.find_elements(By.XPATH, main_heading_xpath)
        main_item = []
        for all_item in main_heading_xpath:
            test = all_item.text
            main_item.append(test)
        result = list(filter(None, main_item)) # none use for remove blank space or index from list
        print(result)
        for index in result:
            text = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{index}')]"
            print(text)
            visible = self.driver.find_element(By.XPATH, text).is_displayed()
            if visible == True:
                self.driver.find_element(By.XPATH, text).click()
                time.sleep(2)
                # self.driver.find_elements(By.XPATH, main_heading_xpath)
                side_bar_item = self.driver.find_elements(By.XPATH, "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//li//a")
                # multi_checkbox_from_ui_status = multi_checkbox_from_ui.is_displayed()
                all_bar_item = []
                for get_bar_item in side_bar_item:
                    test = get_bar_item.get_attribute('href')
                    test = (test.replace('https://admin-demo.nopcommerce.com/Admin',''))
                    all_bar_item.append(test)
                # result = list(filter(None, all_bar_item)) # none use for remove blank space or index from list
                print(all_bar_item)

        # for item in all_bar_item:
        #     text = f"//a[contains(@href,'{item}')]"
        #     self.driver.find_element(By.XPATH, text).click()
        #     time.sleep(2)




        # for box in multi_checkbox:
        #     tester = box
        #     xpath_link = self.driver.find_element(By.XPATH, f"//input[contains(@value,'{tester}')]")
        #     xpath_link_status = xpath_link.is_displayed()
        #     if xpath_link_status:
        #         xpath_link.click()
        #     else:
        #         print("No checkbox found")

