from commonTools import getGenerateDicParams

__author__ = 'chenxinli'
__date__ = '2019/6/01'
from test_01_SsoLogin import *


#为供应商录入合同信息
# @unittest.skip("skip Test_04_EntryContract")
# dictParms = getGenerateDicParams()
class Test_05_EntryContract(Tests_StartEnd):

    # 进入供应商申报页面
    def test_01_applyNewSupplier(self):

        '''进入申报'''
        driver.find_element_by_class_name(applySupplier_class).click()
        sleep(1)
        driver.find_element_by_xpath(supplierApply_xpath).click()

        #校验
        actualValue =  driver.find_element_by_xpath(actualValue01_xpath).text
        self.assertEqual(actualValue, excepted01)

        print('===================17')
        sleep(1)

    # 查找已申报的供应商
    def testcase_02_searchSupplier(self):
        driver.find_element_by_xpath(searchSupplierName_xpath).send_keys(supplierName)
        driver.find_element_by_class_name(searchButton_class).click()

        #校验
        actualValue = driver.find_element_by_xpath(actualValue12_xpath).text
        self.assertEqual(actualValue, supplierName)

        print('===================18')
        sleep(1)

    # 录入合同信息
    def testcase_03_entrySupplierContract(self):
        dictParms = getGenerateDicParams()
        driver.find_element_by_xpath(contractButton_xpath).click()
        print('current_window_handle',driver.current_window_handle)
        sleep(1)

        driver.find_element_by_xpath(OANumber_xpath).send_keys(dictParms['no'])
        driver.find_element_by_xpath(ContractNumber_xpath).send_keys(dictParms['no'])
        driver.find_element_by_class_name(contractAttachment_class).send_keys(r'F:\\cxl\\test_pictures\\abcd.pdf')
        sleep(1)
        driver.find_element_by_xpath(contractSubmit_xpath).click()
        print('===================19')
        sleep(1)




