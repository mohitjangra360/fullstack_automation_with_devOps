import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui


class Catalog_Category:

    def __init__(self, driver):
        self.driver = driver

    def user_should_able_to_click_Button(self, value):

        Import_Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, Import_Button).click()
        time.sleep(2)

    def user_should_able_to_click_Exportoptions_Button_expand(self, value):

        Drop_down_btn = "//div[@class='float-right']//button[@data-toggle='dropdown']"
        options_export = f"//div[@class='float-right']//ul//li[contains(., '{value}')]"

        self.driver.find_element(By.XPATH, Drop_down_btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, options_export).click()
        time.sleep(2)

    def user_should_able_to_see_import_popup(self, value):
        POP_UP_DISPLAY = self.driver.find_element(By.XPATH,
                                                  f"//div[@class='modal-dialog']//div//div//h4[contains(text(),'{value}')]").is_displayed()
        if POP_UP_DISPLAY == True:
            assert True
        else:
            assert False

    def user_should_able_to_select_import_file(self, path):
        self.driver.find_element(By.XPATH, "//div[@class='modal-dialog']//form//input[@id='importexcelfile']").send_keys(f'{path}')
        time.sleep(2)

    def user_should_able_to_select_picture_file(self, path):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='qq-upload-button-selector btn bg-gradient-green']").click()
        time.sleep(4)
        pyautogui.write(fr"{path}")
        pyautogui.press('enter')
        time.sleep(2)

    def user_should_able_to_click_button_of_Import(self, value):
        self.driver.find_element(By.XPATH, f"//div[@class='modal-footer']//button[contains(.,'{value}')]").click()

    def user_should_able_to_see_error_message_of_Import(self, childitem):
        ErrorMessage_1 ='×\nFor security purposes, the feature you have requested is not available on the demo site.'
        ErrorMessage_2 ='×\nPlease upload a file'
        ErrorMessage_3 ='×\nSequence contains no elements'
        SuccessfulMessage =f'×\n{childitem} have been imported successfully.'

        Error_POPUP_text = "//div[@class='alert alert-danger alert-dismissable']"
        Success_popup_text = "//div[@class='alert alert-success alert-dismissable']"

        if 'alert alert-danger alert-dismissable' in self.driver.page_source:
            geterrorValue = self.driver.find_element(By.XPATH, Error_POPUP_text)
            item_error_text = geterrorValue.text

            if item_error_text == ErrorMessage_1:
                assert True
            elif item_error_text == ErrorMessage_2:
                assert True
            elif item_error_text == ErrorMessage_3:
                assert True
            else:
                assert False
        else:
            getsuccessValue = self.driver.find_element(By.XPATH, Success_popup_text)
            item_success_text = getsuccessValue.text

            if item_success_text == SuccessfulMessage:
                assert True
            else:
                assert False

    def select_parent_categories(self, first):
        parent_categories_by_xpath = "//select[@id='ParentCategoryId']"
        self.driver.find_element(By.XPATH, parent_categories_by_xpath).click()
        time.sleep(2)
        ParentCategories_list_values = "//select[@id='ParentCategoryId']//option"
        get_manufacturerslistvalues = self.driver.find_elements(By.XPATH, ParentCategories_list_values)
        ParentCategories_values = []
        for allparentcategories_value in get_manufacturerslistvalues:
            manufacturers_text = allparentcategories_value.text
            ParentCategories_values.append(manufacturers_text)
        if first in ParentCategories_values:
            time.sleep(1)
            self.driver.find_element(By.XPATH, f"//select[@id='ParentCategoryId']//option[text()= '{first}']").click()
            time.sleep(2)

    def go_to_childitem_page(self, childitem, parentitem):
        ParentItem = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{parentitem}')]"
        self.driver.find_element(By.XPATH, ParentItem).click()
        time.sleep(1)
        childitem = f"//p[normalize-space()='{childitem}']"
        self.driver.find_element(By.XPATH, childitem).click()
        time.sleep(3)

    def user_should_able_to_see_Button(self, value):

        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_button = self.driver.find_element(By.XPATH, Button).is_displayed()
        if display_button == True:
            assert True
        else:
            assert False

    def user_should_able_to_click_Delete_Button(self, value):

        if 'dataTables_empty' in self.driver.page_source:
            Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
            self.driver.find_element(By.XPATH, Button).click()
            time.sleep(3)
        else:
            Checkbox_values = "//tbody//input[@class='checkboxGroups']"
            get_checkboxvalues = self.driver.find_elements(By.XPATH, Checkbox_values)
            Value_list=[]

            for all_value in get_checkboxvalues:
                value_text = all_value.get_attribute('value')
                Value_list.append(value_text)
                print(Value_list)

            time.sleep(2)
            self.driver.find_element(By.XPATH, f"//tbody//input[@value= {Value_list[0]}]").click()
            time.sleep(2)

            Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
            self.driver.find_element(By.XPATH, Button).click()
            time.sleep(5)

    def user_should_able_to_delete_selected_Delete_Button(self, value):
        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, Button).click()
        time.sleep(3)

    def user_should_able_to_click_YES_delete_popup(self):
        Click_YES = "//div[@class='modal-content']//div[@class='modal-footer']//button[contains(text(), 'Yes')]"
        Click_OK = "//div[@id='nothingSelectedAlert-action-alert']//div[@class='modal-footer']//span[contains(text(), 'Ok')]"

        nothing_selected_popUP = "//div[@id='nothingSelectedAlert-info']"
        self.driver.find_element(By.XPATH, Click_YES).click()
        time.sleep(2)

        if nothing_selected_popUP in self.driver.page_source:
            self.driver.find_element(By.XPATH, Click_OK).click()
        else:
            print("deleted done")

    def select_deletecheckbox_by_name(self, fullname):

        if 'dataTables_empty' in self.driver.page_source:
            Button = f"//div[@class='float-right']//*[text()[contains(.,'Delete (selected)')]]"
            self.driver.find_element(By.XPATH, Button).click()
            time.sleep(3)
        else:
            full_name = f"//div[@id='categories-grid_wrapper']//div//table//tbody//tr//*[text()='{fullname}']//..//input"
            get_fullname = self.driver.find_elements(By.XPATH, f"{full_name}")
            checkboxvalue = []
            for n in get_fullname:
                name_text = n.get_attribute('value')
                checkboxvalue.append(name_text)
                access_box= f"//div[@id='categories-grid_wrapper']//div//table//tbody//tr//*[text()='{fullname}']//..//input[@value='{checkboxvalue[0]}']"
                while True:
                    time.sleep(3)
                    try:
                        self.driver.find_element(By.XPATH, f"{access_box}").click()
                        time.sleep(2)
                        break
                    except Exception:
                        self.driver.find_element(By.XPATH, "//div[@id='products-grid_paginate']//li[@id='products-grid_next']//a").click()

    def search_result_by_Published_Only_and_Verify(self):
        published_value = "//div[@id='categories-grid_wrapper']//div//table//tbody//tr//td[3]//i"
        get_fullname = self.driver.find_elements(By.XPATH, f"{published_value}")
        checkboxvalue = []
        for n in get_fullname:
            boolen_text = n.get_attribute('nop-value')
            checkboxvalue.append(boolen_text)
            print(checkboxvalue)
            for value in checkboxvalue:
                if 'true' in value:
                    assert True
                else:
                    assert False

    def Verify_downloaded_file(self, path):
        while not os.path.exists(r'C:\Users\User\Downloads'):
            time.sleep(2)
        # check file
        if os.path.isfile(fr'{path}'):
            assert True
        else:
            print("File download is not completed")

        os.remove(fr'{path}')

    def i_set_display_order(self, order):
        self.driver.find_element(By.XPATH, "//input[@id='DisplayOrder']//..//input").send_keys(order)

    def click_Show_on_home_page_checkbox(self):
        tab_click = "//div[@id='category-display']//button[@data-card-widget='collapse']"
        tabs = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Show on home page')]").is_displayed()
        if tabs:
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class='form-group row advanced-setting']//span[@data-valmsg-for='ShowOnHomepage']//..//input[@id='ShowOnHomepage']").click()
            time.sleep(2)
        else:
            self.driver.find_element(By.XPATH, f"{tab_click}").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@class='form-group row advanced-setting']//span[@data-valmsg-for='ShowOnHomepage']//..//input[@id='ShowOnHomepage']").click()
            time.sleep(2)

    def allow_customers_to_select_page_size(self):
        tabs = self.driver.find_element(By.XPATH, "//div[@id='category-display']//i[@class='fa toggle-icon fa-minus']").is_displayed()
        tab_click = "//div[@class='card-header with-border clearfix']//div[contains(text(), 'Display')]"
        if tabs:
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@id='pnlPageSizeOptions']//span[@data-valmsg-for='PageSizeOptions']//..//input[@id='PageSizeOptions']").clear()
            self.driver.find_element(By.XPATH, "//div[@id='pnlPageSizeOptions']//span[@data-valmsg-for='PageSizeOptions']//..//input[@id='PageSizeOptions']").send_keys("6,8,9")
        else:
            self.driver.find_element(By.XPATH, f"{tab_click}").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@id='pnlPageSizeOptions']//span[@data-valmsg-for='PageSizeOptions']//..//input[@id='PageSizeOptions']").clear()
            self.driver.find_element(By.XPATH, "//div[@id='pnlPageSizeOptions']//span[@data-valmsg-for='PageSizeOptions']//..//input[@id='PageSizeOptions']").send_keys("6,8,9")


    # CREATED BY RUPALI
    def i_should_see_export_to_xml(self):
        export_to_xml_xpath = "//a[normalize-space()='Export to XML']"
        export_to_xml = self.driver.find_element(By.XPATH, export_to_xml_xpath).is_displayed()
        if export_to_xml:
            assert True
        else:
            assert False

    # CREATED BY RUPALI
    def i_should_see_export_to_excel(self):
        export_to_excel_xpath = "//a[normalize-space()='Export to Excel']"
        export_to_excel = self.driver.find_element(By.XPATH, export_to_excel_xpath).is_displayed()
        if export_to_excel:
            assert True
        else:
            assert False

    # CREATED BY RUPALI
    def i_should_able_to_select_import_file(self, path):
        self.driver.find_element(By.XPATH,
                                 "//div[@class='modal-dialog']//form//input[@id='importexcelfile']").send_keys(
            f'{path}')
        time.sleep(2)

    # CREATED BY RUPALI
    def i_should_able_to_click_button_of_Import_from_excel(self, value):
        self.driver.find_element(By.XPATH, f"//div[@class='modal-footer']//button[contains(.,'{value}')]").click()

    # CREATED BY RUPALI
    def i_should_able_to_see_error_message_of_Import(self, childitem):
        ErrorMessage_1 = '×\nFor security purposes, the feature you have requested is not available on the demo site.'
        ErrorMessage_2 = '×\nPlease upload a file'
        ErrorMessage_3 = '×\nSequence contains no elements'
        SuccessfulMessage = f'×\n{childitem} have been imported successfully.'

        Error_POPUP_text = "//div[@class='alert alert-danger alert-dismissable']"
        Success_popup_text = "//div[@class='alert alert-success alert-dismissable']"

        if 'alert alert-danger alert-dismissable' in self.driver.page_source:
            get_error_value = self.driver.find_element(By.XPATH, Error_POPUP_text)
            item_error_text = get_error_value.text

            if item_error_text == ErrorMessage_1:
                assert True
            elif item_error_text == ErrorMessage_2:
                assert True
            elif item_error_text == ErrorMessage_3:
                assert True
            else:
                assert False
        else:
            get_success_value = self.driver.find_element(By.XPATH, Success_popup_text)
            item_success_text = get_success_value.text

            if item_success_text == SuccessfulMessage:
                assert True
            else:
                assert False

    # CREATED BY RUPALI
    def i_should_able_to_enter_category_name_in_Search(self, name):
        self.driver.find_element(By.XPATH, "//input[@id='SearchCategoryName']").send_keys(f'{name}')

    # CREATED BY RUPALI
    def i_should_see_published_field_and_select_value(self, publish):
        if publish == 'All':
            self.driver.find_element(By.XPATH, "//button[@id='search-categories']").click()
        elif publish == 'Published only':
            select = Select(self.driver.find_element(By.XPATH, "//select[@id='SearchPublishedId']"))
            select.select_by_visible_text(publish)
        elif publish == 'Unpublished only':
            select = Select(self.driver.find_element(By.XPATH, "//select[@id='SearchPublishedId']"))
            select.select_by_visible_text(publish)

    # CREATED BY RUPALI
    def i_see_search_result(self):
        # row_data = self.driver.find_elements(By.XPATH, "//div[@id='categories-grid_wrapper']//div//table//tbody//tr")

        if 'No data available in table' in self.driver.page_source:
            print("no data in table")
        else:
            no_of_row = self.driver.find_elements(By.XPATH,
                                                  "//div[@id='categories-grid_wrapper']//div//table//tbody//tr")
            length = len(no_of_row)
            print(length)

    # CREATED BY RUPALI
    def i_should_click_on_Export_to_XML(self, export):
        export_to_xpath = f"//a[normalize-space()='{export}']"
        self.driver.find_element(By.XPATH, export_to_xpath).click()

    # CREATED BY RUPALI
    def i_should_verify_download_file(self):
        while not os.path.exists(r'C:\Users\rupal\Downloads'):
            time.sleep(2)
        # check file
            if os.path.isfile(r'C:\Users\rupal\Downloads\categories.xlsx'):
                print("File download is completed")
            else:
                print("File download is not completed")
        os.remove(r'C:\Users\rupal\Downloads\categories.xlsx')

    # CREATED BY RUPALI
    def i_should_see_category_table(self):
        category_table_xpath = "//div[@id='categories-grid_wrapper']//div[@class='row']"
        table_displayed = self.driver.find_element(By.XPATH, category_table_xpath).is_displayed()
        if table_displayed:
            assert True
        else:
            assert False

    # CREATED BY RUPALI
    def i_should_edit_by_category(self, categoryfullname, clickedit):
        categoryname = "//div[@id='categories-grid_wrapper']//div//table//tbody//tr//td[5]"
        get_categoryname = self.driver.find_elements(By.XPATH, f"{categoryname}")
        names_category = []
        for n in get_categoryname:
            name_text = n.text
            names_category.append(name_text)
        edit_button = f"//div[@id='categories-grid_wrapper']//div//table//tbody//tr[contains(., '{categoryfullname}')]//td[contains(., '{clickedit}')]"
        while True:
            time.sleep(3)
            try:
                self.driver.find_element(By.XPATH, f"{edit_button}").click()
                break
            except Exception:
                self.driver.find_element(By.XPATH,
                                         "//div[@id='categories-grid_paginate']//li[@id='categories-grid_next']//a").click()
            print("Product not in database which you entered")

    # CREATED BY RUPALI
    def verify_success_save_category(self):
        success_text_1 = "The category has been updated successfully."
        success_text_2 = "The new category has been added successfully."
        Success_popup_text_xpath = "//div[@class='alert alert-success alert-dismissable']"
        get_success_Value = self.driver.find_element(By.XPATH, Success_popup_text_xpath)
        item_success_text = get_success_Value.text
        if 'alert alert-success alert-dismissable' in self.driver.page_source:
            assert True
            print(success_text_1)
        elif item_success_text == success_text_2:
            assert True
            print(success_text_2)
        else:
            assert False

    # CREATED BY RUPALI
    def i_should_able_to_click_save(self, btn):
        if btn == 'Save':
            self.driver.find_element(By.XPATH, f"//button[normalize-space()='{btn}']").click()
        elif btn == 'Save and Continue Edit':
            self.driver.find_element(By.XPATH, f"//button[normalize-space()='{btn}']").click()

    # CREATED BY RUPALI
    def i_should_able_to_enter_category_name_as(self, field):
        name_xpath = "//label[normalize-space()='Name']"
        name_display = self.driver.find_element(By.XPATH, name_xpath).is_displayed()
        if name_display:
            self.driver.find_element(By.XPATH, "//input[@id='Name']").clear()
            self.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(f'{field}')
        else:
            self.driver.find_element(By.XPATH, "//div[contains(text(),'Category info')]").click()
            if name_display:
                self.driver.find_element(By.XPATH, "//input[@id='Name']").clear()
                self.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(f'{field}')

    # CREATED BY RUPALI
    def i_should_able_to_select_parent_category_as(self, parent):
        parent_category_xpath = "//select[@id='ParentCategoryId']"
        select = Select(self.driver.find_element(By.XPATH, parent_category_xpath))
        select.select_by_visible_text(parent)

    # CREATED BY RUPALI
    def i_should_able_to_select_checkbox_under_category(self, checkbox, value):
        checkbox_xpath = f"//label[normalize-space()='{checkbox}']"
        checkbox_displayed = self.driver.find_element(By.XPATH, checkbox_xpath).is_displayed()
        if checkbox_displayed:
            if value == 'Published':
                self.driver.find_element(By.XPATH, f"//input[@id='{value}']").click()
            elif value == 'IncludeInTopMenu':
                self.driver.find_element(By.XPATH, f"//input[@id='{value}']").click()
            elif value == 'PriceRangeFiltering':
                self.driver.find_element(By.XPATH, f"//input[@id='{value}']").click()
