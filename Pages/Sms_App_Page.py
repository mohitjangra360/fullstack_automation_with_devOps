import time
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

class SMSAPP_Demo:

    username_by_id = "username"
    password_by_id = "password"
    login_btn_by_Xpath = "//input[@id='Login']"
    global tabmenu_list
    global record
    global curr_time
    tabmenu_list = []

    def __init__(self, driver):
        self.driver = driver

    def setSFUsername(self, username):
        self.driver.find_element(By.ID, self.username_by_id).clear()
        self.driver.find_element(By.ID, self.username_by_id).send_keys(username)

    def setSFPassword(self, password):
        self.driver.find_element(By.ID, self.password_by_id).clear()
        self.driver.find_element(By.ID, self.password_by_id).send_keys(password)

    def clickOnSFLogin_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_by_Xpath).click()
        time.sleep(4)

    def classicpage(self):
        expected_login_successful_result = "Home | Salesforce"
        actual_login_successful_result = self.driver.title
        time.sleep(4)
        if expected_login_successful_result == actual_login_successful_result:
            print("login successfully,we're in Lightining")
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, "uiImage").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[text()='Switch to Salesforce Classic']").click()
            time.sleep(3)
        else:
            print("Login Successfully,we,re in Classic")

    def Verify_user_on_App_layout(self, menu):
        time.sleep(2)
        layout_value = self.driver.find_element(By.XPATH, "//div[@id='tsidButton']//span")
        menubar_value = layout_value.text
        if menubar_value == menu:
            assert True
        else:
            menubutton = "//div[@class='multiforce']//div[@id='tsidButton']"
            self.driver.find_element(By.XPATH, f"{menubutton}").click()
            time.sleep(2)
            menuvalue = "//div[@class='multiforce']//div[@id='tsid-menuItems']//a"
            get_menuvalue = self.driver.find_elements(By.XPATH, f"{menuvalue}")
            menuvalue_list=[]
            for value in get_menuvalue:
                menuname = value.text
                menuvalue_list.append(menuname)
            if menu in menuvalue_list:
                self.driver.find_element(By.XPATH, f"//div[@class='multiforce']//div[@id='tsid-menuItems']//a[text()='{menu}']").click()
                time.sleep(2)
            else:
                assert False

    def click_object(self, object):
        time.sleep(2)
        tabmenus = "//div[@id='tabContainer']//ul//li//a"
        get_tabmenu_value = self.driver.find_elements(By.XPATH, f"{tabmenus}")
        for tabvalue in get_tabmenu_value:
            tabname = tabvalue.text
            tabmenu_list.append(tabname)

        if object in tabmenu_list:
            self.driver.find_element(By.XPATH, f"//div[@id='tabContainer']//ul//li//a[text()='{object}']").click()
            time.sleep(2)
        else:
            pagetitle = self.driver.title
            if object in pagetitle:
                assert True
            else:
                assert False

    def click_go_and_verify_selected(self, select):
        go = "//div[@class='bFilterView']//input[@title='Go!']"
        selected = "//div[@class='bFilterView']//select//option[@selected='selected']"
        selected_text = self.driver.find_element(By.XPATH, f"{selected}")
        get_text = selected_text.text
        time.sleep(3)
        if 'tryLexDialog' in self.driver.page_source:
            self.driver.find_element(By.XPATH, "//div[@id='tryLexDialog']//div//a[@title='Close']").click()
            time.sleep(2)
        else:
            pass
        if select == get_text:
            self.driver.find_element(By.XPATH, f"{go}").click()
            time.sleep(2)
        else:
            self.driver.find_element(By.XPATH, "//div[@class='bFilterView']//select[@title='View:']").click()
            time.sleep(2)
            get_values = self.driver.find_elements(By.XPATH, "//div[@class='bFilterView']//select//option")
            value_list=[]
            for selectvalue in get_values:
                selectedname = selectvalue.text
                value_list.append(selectedname)
            if select in value_list:
                self.driver.find_element(By.XPATH, f"//div[@class='bFilterView']//select//option[text()='{select}']").click()
                time.sleep(2)
            else:
                assert False

    def click_any_object_record(self, record):
        pageurl = self.driver.current_url
        spliturl = pageurl.split("=")
        listvalues = f"//div[@id='{spliturl[1]}_grid']//table[@class='x-grid3-row-table']//tr//td[4]//span"
        no_of_records = self.driver.find_elements(By.XPATH, f"{listvalues}")
        list_of_records = []
        for v in no_of_records:
            values = v.text
            list_of_records.append(values)
        if record in list_of_records:
            self.driver.find_element(By.XPATH, f"{listvalues}[text()='{record}']").click()
            time.sleep(2)
        else:
            assert False

    def click_sendsms_button(self):
        self.driver.find_element(By.NAME, "tdc_tsw__send_sms").click()
        time.sleep(2)

    def verify_sendsms_pagedetails(self, s_number, m_type, f_type, d_type, t_type):
        if "Sender Phone" in self.driver.page_source:
            self.driver.find_element(By.XPATH, "//div[@class='form-group']//label[text()='Sender Phone']//..//span[@role='presentation']").click()
            time.sleep(2)
            sendernumbers = "//div[@class='form-group']//label[text()='Sender Phone']//..//select//option"
            no_of_sendernumbers = self.driver.find_elements(By.XPATH, f"{sendernumbers}")
            sender_numbers_list =[]
            for s in no_of_sendernumbers:
                numbers = s.text
                spliting = numbers.split(" ")
                splitnumber = spliting[0]
                sender_numbers_list.append(splitnumber)
            if s_number in sender_numbers_list:
                self.driver.find_element(By.XPATH, f"//span[@class='select2-dropdown select2-dropdown--below']//li[text()='{s_number}']").click()
                time.sleep(3)
            else:
                print("Sender number is not matched,Please check SMSAppData")
                assert False
        else:
            pass

        textfield = self.driver.find_element(By.XPATH, "//div[@class='form-group']//label[text()='Mobile/Phone Number']//following::input[contains(@name,'phonenumbers')]")
        if textfield == '':
            print("Mobile/Phone number field is blank,select number")
            assert False
        else:
            pass

        Message_type_path = "//div[@class='form-group']//label[text()='Channel']//..//select[contains(@name,'selectMessageType')]"
        Message_type = self.driver.find_element(By.XPATH, f"{Message_type_path}")
        if Message_type.is_enabled():
            self.driver.find_element(By.XPATH, f"{Message_type_path}").click()
            time.sleep(2)
            messagetypes = "//div[@class='form-group']//label[text()='Channel']//..//select//option"
            no_of_messagetypes = self.driver.find_elements(By.XPATH, f"{messagetypes}")
            messagetypes_list =[]
            for m in no_of_messagetypes:
                types = m.text
                messagetypes_list.append(types)
            if m_type in messagetypes_list:
                self.driver.find_element(By.XPATH, f"//div[@class='form-group']//label[text()='Channel']//..//select//option[text()='{m_type}']").click()
                time.sleep(2)
            else:
                print("Channel is not matched,Please check SMSAppData")
                assert False
        else:
            print("Channel field is disabled")
            pass

        folder_type_path = "//div[@class='form-group']//label[text()='Folder']//..//select[contains(@name,'selectFolderId')]"
        folder_type = self.driver.find_element(By.XPATH, f"{folder_type_path}")
        if folder_type.is_enabled():
            self.driver.find_element(By.XPATH, f"{folder_type_path}").click()
            time.sleep(3)
            foldertypes = "//div[@class='form-group']//label[text()='Folder']//..//select//option"
            no_of_folderstypes = self.driver.find_elements(By.XPATH, f"{foldertypes}")
            folders_list =[]
            for f in no_of_folderstypes:
                types = f.text
                folders_list.append(types)
            if f_type in folders_list:
                self.driver.find_element(By.XPATH, f"//div[@class='form-group']//label[text()='Folder']//..//select//option[text()='{f_type}']").click()
                time.sleep(2)
            else:
                print("Folder is not matched,Please check SMSAppData")
                assert False
        else:
            print("Folder field is disabled")

        Drip_type_path = "//div[@class='form-group']//label[text()='Drip Campaign']//..//select[contains(@name,'selectdripId')]"
        Drip_type = self.driver.find_element(By.XPATH, f"{Drip_type_path}")
        if Drip_type.is_enabled():
            self.driver.find_element(By.XPATH, f"{Drip_type_path}").click()
            time.sleep(2)
            driptypes = "//div[@class='form-group']//label[text()='Folder']//..//select//option"
            no_of_dripstypes = self.driver.find_elements(By.XPATH, f"{driptypes}")
            drip_list =[]
            for d in no_of_dripstypes:
                types = d.text
                drip_list.append(types)
            if d_type in drip_list:
                self.driver.find_element(By.XPATH, f"//div[@class='form-group']//label[text()='Drip Campaign']//..//select//option[text()='{d_type}']").click()
                time.sleep(2)
            else:
                print("Drip is not matched,Please check SMSAppData")
                assert False
        else:
            print("Drip field is disabled")

        Template_type_path = "//div[@class='form-group']//label[text()='SMS Template']//..//select[contains(@name,'selectFolderTemplateSelectList')]"
        Template_type = self.driver.find_element(By.XPATH, f"{Template_type_path}")
        if Template_type.is_enabled():
            self.driver.find_element(By.XPATH, f"{Template_type_path}").click()
            time.sleep(2)
            templatetypes = "//div[@class='form-group']//label[text()='Folder']//..//select//option"
            no_of_temaplatestypes = self.driver.find_elements(By.XPATH, f"{templatetypes}")
            template_list =[]
            for t in no_of_temaplatestypes:
                types = t.text
                template_list.append(types)
            if t_type in template_list:
                self.driver.find_element(By.XPATH, f"//div[@class='form-group']//label[text()='SMS Template']//..//select//option[text()='{t_type}']").click()
                time.sleep(2)
            else:
                print("Template is not matched,Please check SMSAppData")
                assert False
        else:
            print("Template field is disabled")

    def click_send_button_on_detailpage(self,record):
        global curr_time
        self.driver.find_element(By.XPATH, "//div[@class='mr-0 emojiParent']//textarea").send_keys("testing automation message")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='c_card-footer text-right']//input[@value='Send']").click()
        time.sleep(10)
        curr_time = datetime.now().strftime("%#I:%M %p")
        contact_page_title = f"Contact: {record} ~ Salesforce - Developer Edition"
        get_page_title = self.driver.title
        if contact_page_title == get_page_title:
            assert True
        else:
            print("There is some error in sending message")
            assert False

    def verify_outgoing_history(self):
        pageurl = self.driver.current_url
        spliturl = pageurl.split("=")
        listvalues = f"//div[@id='{spliturl[1]}_grid']//table[@class='x-grid3-row-table']//tr//td[5]//div"
        no_of_records = self.driver.find_elements(By.XPATH, f"{listvalues}")
        list_of_records = []
        for v in no_of_records:
            values = v.text
            splitvalue = values.split(",")
            value = splitvalue[1]
            value_remove_space = value.strip()
            list_of_records.append(value_remove_space)
        if curr_time in list_of_records:
            desc_path = "//div[@id='00B5g00000kDzxC_grid']//tr//td[5][contains(@class,'DESC')]"
            if "00N5g00000b5uH2 DESC" in self.driver.page_source:
                self.driver.find_element(By.XPATH, f"//div[@id='{spliturl[1]}_grid']//table[@class='x-grid3-row-table']//tr//td[4]//span[text() = 'Outgoing']//preceding::td//div[contains(text(),'{curr_time}')]//preceding::td//span[text()='Outgoing']").click()
                time.sleep(2)
            else:
                self.driver.find_element(By.XPATH,f"//div[@id='{spliturl[1]}_grid']//tr//td[5]//div[@title='Created Date']").click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, f"//div[@id='{spliturl[1]}_grid']//table[@class='x-grid3-row-table']//tr//td[4]//span[text() = 'Outgoing']//preceding::td//div[contains(text(),'{curr_time}')]//preceding::td//span[text()='Outgoing']").click()
                time.sleep(2)
            get_message_id = self.driver.find_element(By.XPATH, "//div[@class='pbBody']//tr[4]//td//div")
            id = get_message_id.text
            if len(id) == 0:
                print("message id not filled")
            else:
                id = get_message_id.text
                print("Message ID is :", id)

            get_source = self.driver.find_element(By.XPATH, "//div[@class='pbBody']//tr[9]//td[4]//div")
            source = get_source.text
            if len(source) == 0:
                print("source not filled")
            else:
                source = get_source.text
                print("Source is :", source)
        else:
            assert False
