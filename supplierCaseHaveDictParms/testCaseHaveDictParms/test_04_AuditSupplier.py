__author__ = 'chenxinli'
__date__ = '2019/6/01'

from test_01_SsoLogin import *

#供应商审核
# @unittest.skip("skip Test_03_AuditSupplier")
class Test_04_AuditSupplier(Tests_StartEnd):

    #进入供应商审核界面
    def testcase_01_intoAuditSupplier(self):
        '''进入审核界面'''
        driver.find_element_by_class_name(applySupplier_class).click()
        sleep(1)
        driver.find_element_by_xpath(auditSupplier_xpath).click()
        actualValue = driver.find_element_by_xpath(actualValue09_xpath).text
        self.assertEqual(actualValue, expectedValue09)

        print('===================13')
        sleep(1)

    #查找创建的供应商
    def testcase_02_searchSupplier(self):
        # driver.find_element_by_xpath(searchSupplierName_path).send_keys(dicton['searchSupplierName'])
        driver.find_element_by_xpath(searchSupplierName_xpath).send_keys(supplierName)
        driver.find_element_by_class_name(searchButton_class).click()

        actualValue = driver.find_element_by_xpath(actualValue10_xpath).text
        self.assertEqual(actualValue,supplierName)

        print('===================14')
        sleep(1)

    #供应商初审
    def testcase_03_auditSupplierFirst(self):
        driver.find_element_by_class_name(review_class).click()
        sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        print('current_url',driver.current_url)

        actualValue = driver.find_element_by_xpath(actualValue11_xpath).text
        self.assertEqual(actualValue,expectedValue11)

        # 将滚动条拖到底部-
        # js1 = "var action=document.documentElement.scrollTop=10000"
        driver.execute_script(js_end)
        sleep(1)

        #定位第一个通过按钮
        # js2 = "$(\".el-radio__input\")[0].click();"
        driver.execute_script(js_firstVerifyOnePass)
        sleep(1)

        #定位第二个通过按钮
        # js3 = "$(\".el-radio__input\")[2].click();"
        driver.execute_script(js_firstVerifyTwoPass)
        sleep(1)

        driver.find_element_by_xpath(submit_xpath).click()
        # driver.switch_to_alert().accept()
        driver.refresh()
        sleep(2)
        driver.find_element_by_xpath(close_xpath).click()
        print('===================15')
        sleep(1)

    #供应商终审
    def testcase_04_auditSupplierSecond(self):

        #切换至第一个页面并进入终审页面
        driver.switch_to.window(driver.window_handles[0])
        print('current_urlaaa', driver.current_url)
        driver.find_element_by_class_name(searchButton_class).click()
        sleep(1)
        driver.find_element_by_class_name(review_class).click()
        sleep(1)

        # 切换至终审页面
        driver.switch_to.window(driver.window_handles[1])
        sleep(1)

        #校验
        actualValue = driver.find_element_by_xpath(actualValue11_xpath).text
        self.assertEqual(actualValue, expectedValue12)

        # 将滚动条拖到底部-
        # js4 = "var action=document.documentElement.scrollTop=10000"
        driver.execute_script(js_end)
        sleep(1)

        #定位第一个通过按钮
        # js2 = "$(\".el-radio__original\")[0].click();"
        driver.execute_script(js_secondVerifyOnePass)
        sleep(1)

        #定位第二个通过按钮
        # js3 = "$(\".el-radio__original\")[2].click();"
        driver.execute_script(js_secondVerifyTwoPass)
        sleep(1)
        driver.find_element_by_xpath(submit_xpath).click()
        driver.refresh()
        sleep(2)
        driver.find_element_by_xpath(close_xpath).click()
        sleep(1)

        #查找此供应商已不存在审批页面
        driver.switch_to.window(driver.window_handles[0])
        sleep(1)
        driver.find_element_by_class_name(searchButton_class).click()
        print('===================16')




