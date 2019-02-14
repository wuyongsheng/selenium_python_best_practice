'''
Created on 2019年2月9日

@author: Administrator
'''
import ddt
import unittest
import os
from selenium import  webdriver
from config import setting
from business.login_business import Login_Bussiness
from util.get_last_report import Get_Latest_Report
from util.send_email import SendEmail
import datetime
from util.HTMLTestRunner import HTMLTestRunner
import time
from config.setting import excel_default_path
from util.excel_operation import Excel_Operation

@ddt.ddt
class Ddtcase(unittest.TestCase):
    ex_oper = Excel_Operation(excel_default_path)
    ex_data = ex_oper.get_data()
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1/zentao/user-login.html')
        self.driver.refresh()
        self.driver.maximize_window()
        self.login_b = Login_Bussiness(self.driver)
        self.driver.implicitly_wait(5)
        
    def tearDown(self):
        for method_name, error in self._outcome.errors:  # case如果执行失败，错误会保存到_outcome.errors 中
            if error:  # 将错误信息截图，保存到指定路径
                case_name = self.username  # case名，即定义好的方法名
                report_error_name = case_name + '.png'
                report_error_path = os.path.join(setting.base_dir,'report',report_error_name)
#                 print("report_error:", report_error_name)
                self.driver.save_screenshot(report_error_path)
        self.driver.quit()
        
#     @ddt.data(["admin","Aa1234"],["admin1","Bb1234"])
    @ddt.data(*ex_data)
    @ddt.unpack
    def test_login_case(self,username,password):
        success = self.login_b.login_success(username,password)
        self.assertTrue(success, '登录失败')
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Ddtcase)
    report_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.html'
    report_file = os.path.join(setting.report_dir,report_name)
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(stream=f,title="This is the first ddt_case report1",description="这个是我们第一次测试报告 --数据驱动",verbosity=2)
        runner.run(suite)
          
    last_report = Get_Latest_Report()
    report_file = last_report.latest_file()
#     print(report_file)
    send = SendEmail()
    send.send_email(report_file)
 
 
# if __name__ == '__main__':
#    unittest.main()   
        
