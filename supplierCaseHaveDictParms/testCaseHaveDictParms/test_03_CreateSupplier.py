__author__ = 'chenxinli'
__date__ = '2019/05/22'

from test_01_SsoLogin import *


# 分支：v.cxl_test20190610001
# 申报新供应商
# @unittest.skip("skip ApplyNewSupplier")
class Test_03_CreateSupplier(Tests_StartEnd):

#进入供应商申报页面
    def test_01_applyNewSupplier(self):
        '''进入申报'''
        driver.find_element_by_class_name(supplier_classname).click()
        driver.find_element_by_xpath(supplierApply_xpath).click()
        sleep(1)

        actualValue =  driver.find_element_by_xpath(actualValue01_xpath).text
        self.assertEqual(actualValue, excepted01)
        print('===================2')
        sleep(1)

    # 填写供应商账号信息
    def test_02_supplierPhone(self):
        '''供应商账号'''
        driver.find_element_by_link_text(newSupplierApply_linktext).click()
        driver.find_elements_by_tag_name('input')[1].send_keys('xxxx')
        driver.find_elements_by_tag_name('input')[2].send_keys('xxxx')

        # 校验
        actualValue =  driver.find_element_by_xpath(actualValue02_xpath).text
        self.assertEqual(actualValue, excepted02)

        driver.find_element_by_xpath(buttonNext1_xpath).click()
        print('===================3')
        sleep(1)

    # 填写供应商基本信息
    def test_03_supplierBasicInfo(self):
        '''供应商基本信息'''
        driver.find_elements_by_tag_name('input')[3].send_keys('陈新利')
        driver.find_elements_by_tag_name('input')[4].send_keys('xxxx')
        driver.find_elements_by_tag_name('input')[5].send_keys('11@qq.com')
        driver.find_elements_by_tag_name('input')[6].send_keys('安贞门')

        #校验
        actualValue =  driver.find_element_by_xpath(actualValue03_xpath).text
        self.assertEqual(actualValue, excepted03)

        driver.find_element_by_xpath(buttonNext2_xpath).click()
        print('===================4')
        sleep(1)

    # 填写供应商合作信息
    def test_04_supplierCooperationInfo(self):
        '''供应商合作信息'''
        driver.find_element_by_xpath(contractList_xpath).click()
        driver.find_element_by_xpath(paperworkChoce_xpath).click()
        driver.find_elements_by_tag_name('input')[8].click()
        driver.find_element_by_xpath(primaryClass_xpath).click()
        sleep(1)
        # 二级分类：叶菜类
        driver.find_element_by_class_name(secondaryclass_class).click()
        # 采购专员
        sleep(1)
        driver.find_element_by_xpath(buyer_xpath).click()
        sleep(1)
        driver.find_element_by_xpath(buyerOne_xpath).click()

        # 将滚动条拖到底部-
        driver.execute_script(js_end)
        sleep(2)

        # 其他信息
        driver.find_element_by_xpath(deliveryType_xpath).click()
        driver.find_element_by_xpath(useSortingApp_xpath).click()

        #校验
        actualValue =  driver.find_element_by_xpath(actualValue04_xpath).text
        self.assertEqual(actualValue, excepted04)

        driver.find_elements_by_tag_name('button')[4].click()
        print('===================5')
        sleep(1)


    def test_05_licenseType(self):
        '''执照类型'''
        driver.find_element_by_xpath( licenseType_xpath).click()

        #校验
        actualValue = driver.find_element_by_xpath(actualValue05_xpath).text
        self.assertEqual(actualValue, excepted05)
        print('===================6')
        sleep(1)

    # 填写营业执照信息
    def test_06_businessLicenseInfo(self):
        '''供应商营业执照信息'''
        # driver.find_element_by_xpath(companyName_xpath).send_keys(dicton['searchSupplierName'])
        driver.find_element_by_xpath(companyName_xpath).send_keys(supplierName)
        driver.find_element_by_xpath( companyType_xpath).click()
        driver.find_element_by_xpath(companyTypeChoice_xpath).click()
        driver.find_element_by_xpath(whetherSource).click()
        driver.find_element_by_xpath(businessLicenseNumber).send_keys('123')
        driver.find_element_by_xpath(businessLicenseAdress).send_keys('安贞门')
        driver.find_element_by_xpath(businessLicenseDeadline).click()
        driver.find_element_by_class_name(businessLicenseDeadlineChoice).click()
        driver.find_elements_by_tag_name('td')[9].click()

        # 将滚动条拖到下拖-
        js2 = "var action=document.documentElement.scrollTop=300"
        driver.execute_script(js2)
        sleep(1)
        driver.find_element_by_class_name(businessLicensePhoto).send_keys(r'F:\\cxl\\test_pictures\\abc.jpg')
        sleep(2)

        # 将滚动条拖到底部-
        # js3 = "var action=document.documentElement.scrollTop=10000"
        driver.execute_script(js_end)
        sleep(1)
        print("11111=========", 7)

        driver.find_element_by_xpath(legalPersonName_xpath).send_keys('法人abc')
        driver.find_element_by_xpath(legalPersonID_xpath).send_keys('xxxxx')
        driver.find_element_by_xpath(IDPhoto_xpath).send_keys(r'F:\\cxl\\test_pictures\\abc.jpg')
        sleep(1)
        driver.find_element_by_xpath(taxNature_xpath).click()
        driver.find_element_by_xpath(taxNatureChoice_xpath).click()
        driver.find_elements_by_tag_name('button')[4].click()
        print('===================7')
        sleep(1)


    # 资质信息
    def test_07_documentType(self):
        '''供应商资质信息'''
        driver.find_element_by_xpath(documentType_xpath).click()

        actualValue = driver.find_element_by_xpath(actualValue5_xpath).text
        self.assertEqual(actualValue, expectedValue5)

        print('===================8')
        sleep(1)

    # 食品生产许可证
    def test_08_foodProductionLicense(self):
        '''食品生产许可证'''
        driver.find_element_by_xpath(foodProductionLicenseDeadline_xpath).click()

        # js4 = "$(\".el-icon-d-arrow-right\").click();"
        driver.execute_script(js4)

        # js5 = "$(\".current\").click();"
        driver.execute_script(js5)

        driver.find_element_by_xpath(foodProductionLicensePhoto_xpath).send_keys(r'F:\\cxl\\test_pictures\\abc.jpg')

        actualValue = driver.find_element_by_xpath(actualValue06).text
        self.assertEqual(actualValue,expectedValue06)

        print('===================9')
        sleep(1)
        driver.find_elements_by_tag_name('button')[4].click()

    # 结算信息
    def test_09_billInfo(self):
        '''结算信息'''
        driver.find_element_by_xpath(invoiceType_xpath).click()
        driver.find_element_by_xpath(paymentMethod_xpath).click()
        driver.find_element_by_xpath(marginType_xpath).click()
        driver.find_element_by_xpath(accountStartingDate_xpath).click()
        driver.find_element_by_xpath(nature_xpath).click()
        driver.find_element_by_xpath(accountDays_xpath).click()
        driver.find_element_by_xpath(accountDaysChoice_xpath).click()
        driver.find_element_by_xpath(deferredPaymentDays_xpath).send_keys('3')

        actualValue = driver.find_element_by_xpath(actualValue07_xpath).text
        self.assertEqual(actualValue, expectedValue07)
        print('===================10')
        sleep(1)

    # 开户许可证
    def testcase_10_accountOpeningInfo(self):
        '''开户许可证'''
        # 将滚动条拖到下拖-
        # js6 = "var action=document.documentElement.scrollTop=300"
        driver.execute_script(js_down300)
        sleep(1)

        driver.find_element_by_xpath(accountNumber_xpath).send_keys('xxx')
        driver.find_element_by_xpath(accountName_xpath).send_keys('xxx')
        driver.find_element_by_xpath(accountBankNumber_xpath).send_keys('xxxx')
        sleep(1)

        # 将滚动条拖到底部-
        # js7 = "var action=document.documentElement.scrollTop=5000"
        driver.execute_script(js_end)
        sleep(1)

        driver.find_element_by_xpath(bankName_xpath).send_keys(r'F:\\cxl\\test_pictures\\abc.jpg')
        sleep(1)

        actualValue = driver.find_element_by_xpath(actualValue08_xpath).text
        self.assertEqual(actualValue, expectedValue08)

        driver.find_elements_by_tag_name('button')[4].click()
        print('===================11')
        sleep(1)

# 查询已创建的供应商
    def testcase_11_searchSupplierCreated(self):
        driver.switch_to.window(driver.window_handles[0])
        print('current_urlaaa', driver.current_url)
        sleep(1)
        driver.find_element_by_xpath(searchSupplierName_xpath).send_keys(supplierName)
        sleep(1)
        # driver.find_elements_by_tag_name('input')[0].send_keys(supplierName)
        driver.find_element_by_class_name(searchButton_class).click()
        print('===================12')
        sleep(1)

# if __name__=='__main__':
# 	unittest.main()