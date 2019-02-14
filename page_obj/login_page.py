'''
Created on 2019年2月9日

@author: Administrator
'''
from base.find_element import FindElement
from selenium import webdriver

class LoginPage(object):
    def  __init__(self,driver):
        self.driver = driver
        self.fd = FindElement(self.driver)
        
    def get_username_element(self):
        return self.fd.get_Element('username')
        
    def get_password_element(self):
        return self.fd.get_Element("password")
    
    def get_submit_element(self):
        return self.fd.get_Element('submit')
    
    

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lg = LoginPage(driver)
#     driver.get('http://127.0.0.1/zentao/user-login.html')
#     lg.get_username_element().send_keys('admin')
#     lg.get_password_element().send_keys('Aa1234')
#     lg.get_submit_element().click()
#     driver.quit()

        
    



