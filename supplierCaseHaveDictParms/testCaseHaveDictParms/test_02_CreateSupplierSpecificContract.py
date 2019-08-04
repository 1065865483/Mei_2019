from commonParms import *
from StartEnd import *
from selenium import webdriver
from time import sleep,ctime
from selenium.common.exceptions import NoSuchElementException
from test_01_SsoLogin import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# driver = webdriver.Firefox()
# driver = webdriver.Chrome()

# @unittest.skip("skip Test_02_CreateSupplierSpecificContract")
#创建供应商专用审批单
class Test_02_CreateSupplierSpecificContract(Tests_StartEnd):

    def test_01_enterSsoLogin(self):
        '''登录'''
        driver.get(sso)
        driver.maximize_window()
        self.assertEqual(driver.title,title_excepted02)
        print('===================1')
        sleep(1)

    #进入审批中心界面
    def test_02_enterApprovalCenter(self):
        driver.find_element_by_link_text(approvalCenter_LinkText).click()
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])

        #校验
        actualValue = driver.find_element_by_class_name(actualValue13_class).text
        print(actualValue)
        self.assertEqual(actualValue, excepted13)

        print('current_url',driver.current_url)
        sleep(1)

    #进入供应商专用合同审批单界面并填写
    def test_03_entersupplierSpecificContract(self):
        driver.find_element_by_link_text(supplierSpecificContract_LinkText).click()
        sleep(2)
        print('111111111111111',driver.title)
        driver.switch_to.frame(0)
        sleep(1)

        #校验
        actualValue = driver.find_element_by_xpath(actualValue14_xpath).text
        print(actualValue)
        self.assertEqual(actualValue, excepted14)

        driver.find_element_by_name(city_name).send_keys('北京')
        #附件
        driver.find_element_by_class_name(contractAttachment2_class).click()
        sleep(1)

        driver.find_element_by_xpath(uploadContract_xpath).send_keys(r'F:\\cxl\\test_pictures\\abcd.pdf')
        sleep(2)
        driver.find_element_by_xpath(uploadContractConfirm_xpath).click()
        sleep(2)

        #选择总部或子公司
        driver.find_element_by_xpath(choiceCompany_xpath).click()
        # sleep(2)
        driver.find_elements_by_tag_name('li')[3].click()
        driver.find_element_by_name(supplierName_name).send_keys(supplierName)
        driver.find_element_by_name(companyName_name).send_keys('xxx')

        #合同开始时间
        driver.find_element_by_name(contractStartDate_name).click()

        #合同结束日期
        driver.find_element_by_name(contractEndDate_name).click()
        driver.find_element_by_name(contractEndDate_name).send_keys('2022-12-12')
        sleep(1)

        #付款方式
        driver.find_element_by_xpath(contentPaymentMethod_xpath).click()
        driver.find_elements_by_tag_name(choice_tag)[4].click()

        #采购类别
        driver.find_element_by_xpath(purchaseType_xpath).click()
        driver.find_elements_by_tag_name(choice_tag)[9].click()

        #使用模板情况
        driver.find_element_by_xpath(templetType_xpath).click()
        driver.find_elements_by_tag_name(choice_tag)[3].click()

        #合同主要内容
        driver.find_element_by_name(contractContent_name).send_keys('合同内容123')

        #一级分类
        driver.find_element_by_class_name(primaryClass_name).click()
        driver.find_elements_by_tag_name(choice_tag)[6].click()
        sleep(1)
        #提交
        driver.find_element_by_id(submit_id).click()
        driver.refresh()
        print('current_url123', driver.current_url)
        sleep(2)

    #进入我的审批界面
    def test_04_enterMyApproval(self):
        driver.find_elements_by_tag_name(myApproval_tag)[2].click()
        sleep(1)
        driver.find_element_by_xpath(approverName_xpath).send_keys('陈新利')
        driver.find_elements_by_tag_name(search_tag)[3].click()
        sleep(1)
        #单号
        no = driver.find_element_by_xpath(orderNo_xpath).text
        print(no)
        dicNew = {
            'no': no
        }
        file = open('generateDicParams.txt', 'w+')
        file.write(str(dicNew))
        file.close()
        # return no


    # 审批-同意
    def test_05_approvalOrders(self):
        driver.find_elements_by_tag_name(verifyButton_tag)[0].click()
        sleep(2)
        driver.switch_to.frame(0)
        driver.find_element_by_name(agreeButton_name).click()
        driver.find_element_by_id(approveSubmit_id).click()
        driver.refresh()
        sleep(1)


# if __name__=='__main__':
#     unittest.main()
