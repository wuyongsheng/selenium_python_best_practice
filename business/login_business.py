'''
Created on 2019年2月9日

@author: Administrator
'''
from selenium.common.exceptions import NoAlertPresentException
from handle.login_handle import LoginHandle
from selenium import  webdriver

class Login_Bussiness(object):
    def __init__(self,driver):
        self.driver = driver
        self.login_h = LoginHandle(self.driver)
        self.alert_present = False
        
    def user_base(self,username,password):
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.click_submit_btn()
        self.alert_present = self.is_alert(self.driver)
        if self.alert_present :
            return False
        else :
            return True
        
    def login_success(self,username,password):
#         current_handle = self.driver.current_window_handle
        if  self.user_base(username, password) :
            all_handles = self.driver.window_handles
#           print(all_handles)
            for handle in all_handles :
                self.driver.switch_to.window(handle)
#               print(self.driver.title)
                if '我的地盘 ' in self.driver.title:
#                     text =  self.driver.find_element_by_xpath('//*[@id="block2"]/div[1]/div').text
# #                 print(text)
# #                 print('login success !')
#                     if(text == '最新动态'):
                        return True
#         print('login fail')
        return False
    
    
    def is_alert(self,driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return True
        except NoAlertPresentException:
            return False
                
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lb = Login_Bussiness(driver)
#     driver.get('http://127.0.0.1/zentao/user-login.html')
#     lb.user_base('admin', 'Aa1234')
#     if lb.alert_present :
#         print('login fail ! ')
#     else :
#         lb.login_success()
#     driver.quit()