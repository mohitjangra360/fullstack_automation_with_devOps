import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.select import Select


class ProductListPage:

    def __init__(self, driver):
        self.driver = driver

    def i_should_see_product_column(self):
        # to identify headers
        column_list = self.driver.find_elements(By.XPATH, "//div[@class='dataTables_scrollHead']//th")
        # print(len(column_list))
        for i in column_list:
            print(i.text)

    def i_should_select_items_to_display(self, value):
        # select number of items display from show items dropdown
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='products-grid_length']"))
        # select by value
        # select.select_by_value(value)
        select.select_by_visible_text(value)

    def i_verify_selected_items_and_displayed_items(self, valuee):
        # to identify rows in table body
        rows_list = self.driver.find_elements(By.XPATH, "//tbody//tr")
        # verify value and no.of rows
        if len(rows_list) == valuee:
            assert True
        else:
            assert False

    def i_should_able_to_click_on_edit_btn_of_frst_product(self):
        self.driver.find_element(By.XPATH, "(//tbody//tr//a)[1]").click()

    def i_verify_cards_under_advance_mode(self):
        a = self.driver.find_elements(By.XPATH, "//nop-card//div[@class='card-title']")
        card_list = []
        for j in a:
            card_text = j.text
            card_list.append(card_text)
        print(card_list)

    def i_edit_the_fields_under_product_info_card(self, card_name):
        card = self.driver.find_element(By.XPATH, f"//div[@class='card-title' and contains(text(),'{card_name}')]")
        card_status = card.is_displayed
        if card_status:
            assert True

    def i_edit_the_product_name(self, edited_name):
        self.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(f' {edited_name}')

    def i_edit_the_Short_description(self, edited_name):
        self.driver.find_element(By.XPATH, "//textarea[@id='ShortDescription']").send_keys(f' {edited_name}')

    def i_edit_the_Full_description(self, edited_name):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='FullDescription_ifr']"))
        self.driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys(f' {edited_name}')

    def i_edit_SKU(self, edited_name):
        self.driver.find_element(By.XPATH, "//input[@id='Sku']").send_keys(f' {edited_name}')

