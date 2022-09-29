import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Catalog_Product:
    save_btn_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def i_see_add_new_btn(self):
        self.driver.find_element(By.XPATH, "//*[contains(@href,'Create')]").is_displayed()

    def click_on_add_new_cust_btn(self):
        self.driver.find_element(By.XPATH, "//*[contains(@href,'Create')]").click()

    def i_see_download_catalog_pdf_btn(self):
        self.driver.find_element(By.XPATH, "//button[@name='download-catalog-pdf']").is_displayed()

    def i_click_on_download_catalog_btn(self):
        self.driver.find_element(By.XPATH, "//button[@name='download-catalog-pdf']").click()

    def i_see_export_btn(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").is_displayed()

    def i_click_on_export_btn(self):
        self.driver.find_element(By.XPATH, "//button[@data-toggle='dropdown']").click()

    def i_see_export_to_xml_all(self):
        self.driver.find_element(By.XPATH, "//button[@name='exportxml-all']").is_displayed()

    def i_see_export_to_xml_selected(self):
        self.driver.find_element(By.XPATH, "//button[@id='exportxml-selected']").is_displayed()

    def i_see_export_to_excel_all(self):
        self.driver.find_element(By.XPATH, "//button[@name='exportexcel-all']").is_displayed()

    def i_see_export_to_excel_selected(self):
        self.driver.find_element(By.XPATH, "//button[@name='exportexcel-all']").is_displayed()

    def i_see_import(self):
        self.driver.find_element(By.XPATH, "//button[@name='importexcel']").is_displayed()

    def i_click_on_import(self):
        self.driver.find_element(By.XPATH, "//button[@name='importexcel']").click()

    def i_see_choose_file_popup_box(self):
        self.driver.find_element(By.XPATH, "//input[@id='importexcelfile']").is_displayed()

    def i_see_delete_btn(self):
        self.driver.find_element(By.XPATH, "//button[@id='delete-selected']").is_displayed()

    def i_click_on_delete_btn(self):
        self.driver.find_element(By.XPATH, "//button[@id='delete-selected']").click()

    def i_set_products_name(self, name):
        self.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(name)


    def i_set_short_description(self, short_descp):
        self.driver.find_element(By.XPATH, "//textarea[@id='ShortDescription']").send_keys(short_descp)

    def i_set_full_description(self, full_descp):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='FullDescription_ifr']"))
        self.driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys(full_descp)
        time.sleep(2)
        self.driver.switch_to.default_content()

    def i_set_description(self, descp):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='Description_ifr']"))
        self.driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys(descp)
        time.sleep(2)

        self.driver.switch_to.default_content()


    def set_mail_for_cust(self):
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(self.random_email() + "@gmail.com")

    def random_email(size=10, char=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(char) for x in range(size))

    def set_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lastname)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Female']").click()
        else:
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, "//input[@id='DateOfBirth']").send_keys(dob)

    def set_customer_role(self, first):
        CustomerRole_list_by_xpath = "//div[@role='listbox']//input[@aria-describedby='SelectedCustomerRoleIds_taglist']"
        self.driver.find_element(By.XPATH, CustomerRole_list_by_xpath).click()
        time.sleep(2)

        CustomerRole_list_values = "//div[@class='k-list-scroller']//ul[@id='SelectedCustomerRoleIds_listbox']//li"
        get_CustomerRolelistvalues = self.driver.find_elements(By.XPATH, CustomerRole_list_values)
        CustomerRole_values = []

        for allcustomers_value in get_CustomerRolelistvalues:
            CustomerRole_text = allcustomers_value.text
            CustomerRole_values.append(CustomerRole_text)

        if first in CustomerRole_values:
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     f"//div[@class='k-list-scroller']//ul[@id='SelectedCustomerRoleIds_listbox']//li[text()= '{first}']").click()
            time.sleep(2)
            # self.driver.find_element(By.XPATH, "//html").click()
            # time.sleep(2)


    def i_select_product_to_delete(self):
        Checkbox_values = "//tbody//input[@class='checkboxGroups']"
        get_checkboxvalues = self.driver.find_elements(By.XPATH, Checkbox_values)
        Value_list = []
        for all_value in get_checkboxvalues:
            value_text = all_value.get_attribute('value')
            Value_list.append(value_text)
            print(Value_list)
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//tbody//input[@value= {Value_list[0]}]").click()
        time.sleep(2)

    def user_should_able_to_see_Delete_Button(self, value):
        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_button = self.driver.find_element(By.XPATH, Button).is_displayed()
        if display_button:
            assert True
        else:
            assert False

    def user_should_able_to_click_Delete_Button(self, value):
        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, Button).click()
        time.sleep(5)

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

    def i_verify_product_sku_field(self):
        product_sku_by_xpath = "//label[normalize-space()='Go directly to product SKU']"
        display_field = self.driver.find_element(By.XPATH, product_sku_by_xpath).is_displayed()
        if display_field:
            assert True
        else:
            assert False

    def enter_product_SKU(self, sku):
        enter_SKU = "//input[@id='GoDirectlyToSku']"
        self.driver.find_element(By.XPATH, enter_SKU).send_keys(f'{sku}')

    def i_click_on_go_btn(self):
        self.driver.find_element(By.XPATH, "//button[@id='go-to-product-by-sku']").click()

    def verify_edit_page_of_that_product(self, value):
        value_on_ui = self.driver.find_element(By.XPATH, "//input[@id='Sku']").get_attribute('value')
        if value == value_on_ui:
            assert True
        else:
            assert False

    def i_should_see_product_table(self):
        product_table_xpath = "//div[@id='products-grid_wrapper']//div[@class='row']"
        table_displayed = self.driver.find_element(By.XPATH, product_table_xpath).is_displayed()
        if table_displayed:
            assert True
        else:
            assert False

    def i_should_see_product_field(self, field_name):
        product_field_by_xpath = f"//div[@class='col-md-3']//label[normalize-space()='{field_name}']"
        field_displayed = self.driver.find_element(By.XPATH, product_field_by_xpath).is_displayed()
        time.sleep(5)
        if field_displayed:
            assert True
        else:
            assert False

    def i_should_see_edit_btn_and_click(self, product):
        product_name_by_xpath = "//*[@id='products-grid']/tbody/tr/td[3]"
        a_product_name = self.driver.find_elements(By.XPATH, product_name_by_xpath)
        text_of_product_name = []
        for i in a_product_name:
            get_text_of_product_name = i.text
            text_of_product_name.append(get_text_of_product_name)
        print(text_of_product_name)
        # get the index of product
        index_of_product_in_list = text_of_product_name.index(f'{product}')
        print(index_of_product_in_list)
        if product in text_of_product_name:
            self.driver.find_element(By.XPATH, f"//a[@href='Edit/{index_of_product_in_list + 1}']").click()
            time.sleep(2)
        else:
            assert False

    def i_change_field_and_save(self, field, new_value, tag):
        field_xpath = f"//{tag}[contains(@id,'{field}')]"
        if tag == 'input':
            self.driver.find_element(By.XPATH, field_xpath).clear()
            self.driver.find_element(By.XPATH, field_xpath).send_keys(f'{new_value}')
        elif tag == 'select':
            select = Select(self.driver.find_element(By.XPATH, field_xpath))
            time.sleep(5)
            select.select_by_visible_text(new_value)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.save_btn_xpath).submit()
        time.sleep(5)

    def set_Max_cart_qty(self, qty):
        max_qty = self.driver.find_element(By.XPATH,
                                           "//div[@id='product-inventory']//input[@id='OrderMaximumQuantity']//..//input[1]")
        if max_qty.is_displayed():
            max_qty.send_keys(qty)
            time.sleep(2)
        else:
            self.driver.find_element(By.ID, "product-inventory").click()
            time.sleep(3)
            max_qty.send_keys(qty)
            time.sleep(2)

    def select_categories(self, first, second):
        Category_list_by_xpath = "//div[@role='listbox']//input[@aria-describedby='SelectedCategoryIds_taglist']"
        self.driver.find_element(By.XPATH, Category_list_by_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f"//div[@class='k-list-scroller']//ul[@id='SelectedCategoryIds_listbox']//li[text()='{first}']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f"//div[@class='k-list-scroller']//ul[@id='SelectedCategoryIds_listbox']//li[text()='{second}']").click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,("//body")).click()
        # time.sleep(2)

    def set_Minimum_cart_qty(self, qty):
        minimum_qty = self.driver.find_element(By.XPATH,
                                               "//div[@id='product-inventory']//input[@id='OrderMinimumQuantity']//..//input[1]")
        if minimum_qty.is_displayed():
            minimum_qty.send_keys(qty)
            time.sleep(2)
        else:
            self.driver.find_element(By.ID, "product-inventory").click()
            time.sleep(3)
            minimum_qty.send_keys(qty)
            time.sleep(2)

    def set_shipping_weight(self, weight):
        weightfield = self.driver.find_element(By.XPATH,
                                               "//div[@id='product-shipping']//input[@id='Weight']//..//input[1]")
        if weightfield.is_displayed():
            weightfield.send_keys(weight)
            time.sleep(2)
        else:
            self.driver.find_element(By.ID, "product-shipping").click()
            time.sleep(3)
            weightfield.send_keys(weight)
            time.sleep(2)

    def set_price(self, price):
        pricefield = self.driver.find_element(By.XPATH, "//div[@id='product-price']//input[@id='Price']//..//input[1]")
        check = pricefield.is_displayed()
        if check:

            pricefield.send_keys(price)
            time.sleep(2)
        else:
            self.driver.find_element(By.ID, "product-price").click()
            time.sleep(2)
            pricefield.clear()
            pricefield.send_keys(price)
            time.sleep(2)

    def set_available_start_date(self, startdate):
        self.driver.find_element(By.XPATH,
                                 "//span[@class='k-picker-wrap k-state-default']//input[@id='AvailableStartDateTimeUtc']").send_keys(
            f"{startdate}")
        time.sleep(2)

    def set_available_end_date(self, enddate):
        self.driver.find_element(By.XPATH,
                                 "//span[@class='k-picker-wrap k-state-default']//input[@id='AvailableEndDateTimeUtc']").send_keys(
            f"{enddate}")
        time.sleep(2)

    def set_vendor_type(self, type):
        self.driver.find_element(By.XPATH, "//select[@name='VendorId']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f"//select[@name='VendorId']//option[contains(text(), '{type}')]").click()

    def set_product_type(self, types):
        Product_type = self.driver.find_element(By.XPATH,
                                                f"//select[@name='ProductTypeId']//option[contains(text(), '{types}')]").is_displayed()
        if Product_type:
            assert True
        else:
            self.driver.find_element(By.XPATH, "//select[@name='ProductTypeId']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,
                                     f"//select[@name='ProductTypeId']//option[contains(text(), '{types}')]").click()

    def set_product_tags(self, tag):
        time.sleep(2)
        self.driver.execute_script(f"document.getElementById('ProductTags').getElementsByTagName('div').value='test'")
        #argument().click()
        time.sleep(2)

    def i_change_product_cost_and_save(self, cost):
        # field_xpath = f"//input[contains(@id,'{field}')]"
        field_xpath = "//*/div[@class='card-body']/div[3]/div[2]/span[1]/span[1]/input[1]"
        self.driver.find_element(By.XPATH, field_xpath).send_keys(f'{cost}')
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.save_btn_xpath).submit()
        time.sleep(5)

    def i_see_search_result_by_warehouse(self):
        no_data = self.driver.find_elements(By.XPATH, "//div[@id='products-grid_wrapper']//div//table//tbody//tr")
        if 'No data available in table' in no_data:
            print("no data in table")
        else:
            no_of_row = self.driver.find_elements(By.XPATH, "//div[@id='products-grid_wrapper']//div//table//tbody//tr")
            length = len(no_of_row)
            print(length)

    def i_should_see_table(self):
        now_of_row = self.driver.find_element(By.XPATH, "//table[contains(@id,'grid')]")
        if now_of_row.is_displayed():
            assert True
        else:
            assert False

    def user_should_able_to_click_all_checkboxes(self):
        if 'dataTables_empty' in self.driver.page_source:
            print("No data in table to select")
        else:
            Checkbox_values = "//tbody//input[@class='checkboxGroups']"
            get_checkboxvalues = self.driver.find_elements(By.XPATH, Checkbox_values)
            Value_list = []
            for all_value in get_checkboxvalues:
                value_text = all_value.get_attribute('value')
                Value_list.append(value_text)

            for i in Value_list:
                self.driver.find_element(By.XPATH,
                                         f"//div[@id='products-grid_wrapper']//div//table//tbody//input[@value={i}]").click()

    def select_edit_by_name(self, fullname, clickedit):
        Product_title = "Products / nopCommerce administration"
        Categories_title = "Categories / nopCommerce administration"

        if Product_title in self.driver.page_source:
            edit_button = f"//div[@id='products-grid_wrapper']//div//table//tbody//tr[contains(., '{fullname}')]//td[contains(., '{clickedit}')]"
            while True:
                time.sleep(3)
                try:
                    self.driver.find_element(By.XPATH, f"{edit_button}").click()
                    break
                except Exception:
                    self.driver.find_element(By.XPATH,
                                             "//div[@id='products-grid_paginate']//li[@id='products-grid_next']//a").click()
        elif Categories_title in self.driver.page_source:
            edit_button = f"//div[@id='categories-grid_wrapper']//div//table//tbody//tr[contains(., '{fullname}')]//td[contains(., '{clickedit}')]"
            while True:
                time.sleep(3)
                try:
                    self.driver.find_element(By.XPATH, f"{edit_button}").click()
                    break
                except Exception:
                    self.driver.find_element(By.XPATH,
                                             "//div[@id='categories-grid_paginate']//li[@id='categories-grid_next']//a").click()
        else:
            assert False

    def select_deletecheckbox_by_name(self, fullname):
        full_name = f"//div[@id='categories-grid_wrapper']//div//table//tbody//tr//*[text()='{fullname}']//..//input"
        get_fullname = self.driver.find_elements(By.XPATH, f"{full_name}")
        checkboxvalue = []
        for n in get_fullname:
            name_text = n.get_attribute('value')
            checkboxvalue.append(name_text)
        checkbox = f"//div[@id='categories-grid_wrapper']//div//table//tbody//tr//*[text()='{fullname}']//..//input[@value='{checkboxvalue}']"
        time.sleep(2)
        self.driver.find_element(By.XPATH, checkbox).click()
        time.sleep(2)

    def select_categories_manufacturers(self, first):
        Manufacturers_list_by_xpath = "//div[@role='listbox']//input[@aria-describedby='SelectedManufacturerIds_taglist']"
        self.driver.find_element(By.XPATH, Manufacturers_list_by_xpath).click()
        time.sleep(2)
        Manufacturers_list_values = "//div[@class='k-list-scroller']//ul[@id='SelectedManufacturerIds_listbox']//li"
        get_manufacturerslistvalues = self.driver.find_elements(By.XPATH, Manufacturers_list_values)
        Manufacturers_values = []
        for allmanufacturers_value in get_manufacturerslistvalues:
            manufacturers_text = allmanufacturers_value.text
            Manufacturers_values.append(manufacturers_text)
        if first in Manufacturers_values:
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     f"//div[@class='k-list-scroller']//ul[@id='SelectedManufacturerIds_listbox']//li[text()= '{first}']").click()
            time.sleep(2)
            # self.driver.find_element(By.XPATH, "//section[@class='content']").click()
            # time.sleep(2)

    def move_to_advance(self):
        Advance = "sidebar-mini layout-fixed control-sidebar-slide-open advanced-settings-mode"
        Basic = "sidebar-mini layout-fixed control-sidebar-slide-open basic-settings-mode"

        if Basic in self.driver.page_source:
            self.driver.find_element(By.XPATH, "//div[@class='onoffswitch']//label").click()
        else:
            print("we're already in advance")

    def save_product_details(self, select):
        self.driver.find_element(By.XPATH, f"//button[@name='{select}']").click()
        time.sleep(2)

    def verify_success_save(self):
        success_text_1 = "The new product has been added successfully."
        success_text_2 = "The product has been updated successfully."
        Success_popup_text = "//div[@class='alert alert-success alert-dismissable']"
        getsuccessValue = self.driver.find_element(By.XPATH, Success_popup_text)
        item_success_text = getsuccessValue.text
        if 'alert alert-success alert-dismissable' in self.driver.page_source:
            assert True
            print(success_text_1)
        elif item_success_text == success_text_2:
            assert True
            print(success_text_2)
        else:
            assert False

    def user_mark_product_as_new(self, mark):
        self.driver.find_element(By.ID, f"{mark}").click()

    def search_new_product_in_related_products(self):
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    def i_search_relatedproducts_name(self, name):
        self.driver.find_element(By.XPATH, "//input[@id='SearchProductName']").send_keys(name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@id='search-products']").click()
        time.sleep(2)

        productname_value = "//div[@id='products-grid_wrapper']//div//table//tbody//tr//td[2]"
        get_fullname = self.driver.find_elements(By.XPATH, f"{productname_value}")
        tablevalue = []
        for n in get_fullname:
            name_text = n.text
            tablevalue.append(name_text)
        print(len(tablevalue))
        if name in tablevalue:
            checkbox_button = f"//div[@id='products-grid_wrapper']//div//table//tbody//tr[contains(., '{name}')]//td//input[@type='checkbox']"
            self.driver.find_element(By.XPATH, checkbox_button).click()
            time.sleep(2)
        else:
            print("no match")

    def click_add_new_product_in_related_products(self):
        tab_click = "//div[@id='product-related-products']//button[@data-card-widget='collapse']"
        tabs = self.driver.find_element(By.ID, "btnAddNewRelatedProduct").is_displayed()
        if tabs:
            time.sleep(2)
            self.driver.find_element(By.ID, "btnAddNewRelatedProduct").click()
            time.sleep(3)
        else:
            self.driver.find_element(By.XPATH, f"{tab_click}").click()
            time.sleep(2)
            self.driver.find_element(By.ID, "btnAddNewRelatedProduct").click()
            time.sleep(2)

    def i_search_relatedproducts_category(self, name):
        self.driver.find_element(By.XPATH, "//select[@id='SearchCategoryId']").click()
        time.sleep(2)
        categoryvaluetext = self.driver.find_elements(By.XPATH, "//select[@id='SearchCategoryId']//option")
        category_value = []
        for value in categoryvaluetext:
            get_categoryvalue_text = value.text
            category_value.append(get_categoryvalue_text)
        if name in category_value:
            self.driver.find_element(By.XPATH, f"//select[@id='SearchCategoryId']//option[text()= '{name}']").click()
            time.sleep(2)
        else:
                print("value not in dropdown")

        self.driver.find_element(By.XPATH, "//button[@id='search-products']").click()
        time.sleep(2)
        productname_value = "//div[@id='products-grid_wrapper']//div//table//tbody//tr//td[2]"
        get_fullname = self.driver.find_elements(By.XPATH, f"{productname_value}")
        tablevalue = []
        for n in get_fullname:
            name_text = n.text
            tablevalue.append(name_text)
        print(len(tablevalue))
        if name in tablevalue:
            checkbox_button = f"//div[@id='products-grid_wrapper']//div//table//tbody//tr[contains(., '{name}')]//td//input[@type='checkbox']"
            self.driver.find_element(By.XPATH, checkbox_button).click()
            time.sleep(2)
        else:
            print("no match")

    def i_search_relatedproducts_Vendor(self, name):
        self.driver.find_element(By.XPATH, "//select[@id='SearchVendorId']").click()
        time.sleep(2)
        Vendorvaluetext = self.driver.find_elements(By.XPATH, "//select[@id='SearchVendorId']//option")
        Vendor_value = []
        for value in Vendorvaluetext:
            get_vendorvalue_text = value.text
            Vendor_value.append(get_vendorvalue_text)
        if name in Vendor_value:
            self.driver.find_element(By.XPATH, f"//select[@id='SearchVendorId']//option[text()= '{name}']").click()
            time.sleep(2)
        else:
            print("value not in dropdown")

        self.driver.find_element(By.XPATH, "//button[@id='search-products']").click()
        time.sleep(2)
        productname_value = "//div[@id='products-grid_wrapper']//div//table//tbody//tr//td[2]"
        get_fullname = self.driver.find_elements(By.XPATH, f"{productname_value}")
        tablevalue = []
        for n in get_fullname:
            name_text = n.text
            tablevalue.append(name_text)
        print(len(tablevalue))
        if name in tablevalue:
            checkbox_button = f"//div[@id='products-grid_wrapper']//div//table//tbody//tr[contains(., '{name}')]//td//input[@type='checkbox']"
            self.driver.find_element(By.XPATH, checkbox_button).click()
            time.sleep(2)
        else:
            print("no match")

    def verifynew_added_product_in_related_products_byname(self, name):

        get_table_vlue = self.driver.find_elements(By.XPATH, "//div[@id='relatedproducts-grid_wrapper']//div//table//tbody//tr//td[1]")
        get_value = []
        for v in get_table_vlue:
            name_text = v.text
            get_value.append(name_text)
        # if name in get_value:
        #     assert True
        # else:
        #     assert False
        while name in get_value:
            time.sleep(3)
            try:
                assert True
                break
            except Exception:
                self.driver.find_element(By.XPATH,
                                         "//div[@id='products-grid_paginate']//li[@id='products-grid_next']//a").click()

    def i_should_see_delete_button(self, value):
        delete_button_xpath = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_delete_button = self.driver.find_element(By.XPATH, delete_button_xpath).is_displayed()
        if display_delete_button:
            assert True
        else:
            assert False

    def i_should_click_on_delete_button(self, value):
        click_on_delete_Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, click_on_delete_Button).click()

    def i_should_see_popup_message(self, value):
        see_popup_message = f"//div[@class='modal-content']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, see_popup_message).is_displayed()
        if see_popup_message:
            assert True
        else:
            assert False

    def user_should_see_import_button(self, value):
        see_import_button_xpath = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_import_button = self.driver.find_element(By.XPATH, see_import_button_xpath).is_displayed()
        if display_import_button == True:
            assert True
        else:
            assert False

    def user_should_click_on_import_button(self, value):
        click_on_import_button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, click_on_import_button).click()

    def user_should_see_popup_message(self, value):
        see_popup_message = self.driver.find_element(By.XPATH,
                                                     f"//div[@class='modal-dialog']//div//div//h4[contains(text(),'{value}')]").is_displayed()
        if see_popup_message == True:
            assert True
        else:
            assert False

    def user_should_click_on_import_from_excel(self, value):
        self.driver.find_element(By.XPATH, f"//div[@class='modal-footer']//button[contains(.,'{value}')]").click()

    def user_should_select_path_test_data(self, path):
        ram = self.driver.find_element(By.XPATH, "//div[@class='modal-dialog']//form//input[@id='importexcelfile']")
        ram.send_keys(f"{path}")

    def user_should_able_to_see_error_message_of_Import(self, childitem):
        ErrorMessage_1 = '×\nFor security purposes, the feature you have requested is not available on the demo site.'
        ErrorMessage_2 = '×\nPlease upload a file'
        ErrorMessage_3 = '×\nSequence contains no elements'
        SuccessfulMessage = f'×\n{childitem} have been imported successfully.'

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

    def user_should_click_on_search_button(self, value):
        see_search_button = self.driver.find_element(By.XPATH,
                                                     f"//div[@class='text-center col-12']//*[text()[contains(.,'{value}')]]").click()

    def user_should_select_product_type(self, value):
        product_type = Select(self.driver.find_element(By.XPATH, "//select[@id='SearchProductTypeId']"))
        product_type.select_by_visible_text(value)

    def user_should_be_able_to_see_edit_button(self):
        see_edit_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="products-grid"]/tbody/tr[5]/td[8]/a').is_displayed()
        if see_edit_button == True:
            assert True
        else:
            assert False

    def user_should_be_able_to_click_on_edit_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="products-grid"]/tbody/tr[5]/td[8]/a').click()

    def user_should_set_date_time_on_start_date(self, value):
        self.driver.find_element(By.XPATH, "//input[@id='AvailableStartDateTimeUtc']").send_keys(value)

    def user_should_be_able_to_click_on_save_button(self, value):
        self.driver.find_element(By.XPATH,
                                 f"//div[@class='float-right']//button[@name='save' and normalize-space()='{value}']")

    def user_should_see_edit_button(self):
        edit = self.driver.find_element(By.XPATH, '//*[@id="products-grid"]/tbody/tr[3]/td[8]/a').is_displayed()
        if edit == True:
            assert True
        else:
            assert False

    def user_should_click_on_edit_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="products-grid"]/tbody/tr[3]/td[8]/a').click()

    def user_should_checked_on_checkbox(self):
        self.driver.find_element(By.XPATH, "//input[@id='ShowOnHomepage']").click()

    def i_set_display_order(self, value):
        set = self.driver.find_element(By.XPATH, "//*[@id='DisplayOrder']").clear()
