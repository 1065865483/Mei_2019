__author__ = 'chenxinli'
__date__ = '2019/05/22'

from commonTools import getDictionary
# from commonTools import dragScrollBar
from commonParms import *
from StartEnd import *
from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
# driver = webdriver.Chrome()
sleep(1)
dicton = getDictionary()
# @unittest.skip("skip Test_01_SsoLogin")
class Test_01_SsoLogin(Tests_StartEnd):

    def test_01_supplierLogin(self):
        '''登录'''
        driver.get(scm_url)
        driver.add_cookie({'name': name,
                           'value': xxxx,
                           'domain':domain})
        sleep(1)
        driver.get(xxxx)
        driver.maximize_window()

        self.assertEqual(driver.title,title_excepted)
        print('===================1')
        sleep(1)


#
#
# if __name__=='__main__':
#     unittest.main()




