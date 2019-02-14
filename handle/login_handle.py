'''
Created on 2019年2月9日

@author: Administrator
'''
from page_obj.login_page import LoginPage
from selenium import webdriver

class LoginHandle(object):
    
    def __init__(self,driver):
        self.driver = driver
        self.login_p = LoginPage(self.driver)
        
    def send_username(self,username):
        self.login_p.get_username_element().clear()
        self.login_p.get_username_element().send_keys(username)
        
    def send_password(self,password):
        self.login_p.get_password_element().clear()
        self.login_p.get_password_element().send_keys(password)
        
    def click_submit_btn(self):
        self.login_p.get_submit_element().click()
        
        
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lh = LoginHandle(driver)
#     driver.get('http://127.0.0.1/zentao/user-login.html')
#     lh.send_username('admin')
#     lh.send_password('Aa1234')
#     lh.click_submit_btn()