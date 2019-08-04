import unittest
from BSTestRunner import BSTestRunner
import time

#定义测试用例路径
test_dir='./testCaseHaveDictParms'
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == "__main__":
    report_dir='./test_report_supplier'
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'

    #打开文件在报告文件写入测试结果
    with open(report_name,'wb')as f:
        runer=BSTestRunner(stream=f,title="Test Report",description="Test case result")
        runer.run(discover)
    f.close()