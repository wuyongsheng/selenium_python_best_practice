'''
Created on 2019年2月12日

@author: Administrator
'''
from selenium import webdriver
from base.find_element import FindElement
import time

class ActionMethod(object):
    def open_browser(self,browser):
        try:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                self.driver = webdriver.Edge()
        except:
            print('ActionMethodError:没有"{}"这个元素'.format(browser))
            
    def get_url(self,url):
        try:
            self.driver.get(url)
        except:
            print("ActionMethodError: url:{},输入有误".format(url))
            
    def get_element(self,key):
        try:
            find_element = FindElement(self.driver)
            element = find_element.get_Element(key)
            return element 
        except:
            print("ActionMethodError:'{}'元素定位失败".format(key)) 
        
    def element_send_keys(self,value,key):
        try:
            element = self.get_element(key)
            element.send_keys(value)
        except:
            print("ActionMethodError: 输入有误：'{}'".format(value))
            
    def click_element(self,key):
        try:
            self.get_element(key).click()
        except:
            print("ActionMethodError:'{}'元素不存在，无法点击".format(key))    
            
    def sleep_time(self):
        time.sleep(3)
        
    def close_browser(self):
        self.driver.close()
        
    def get_title(self):
        title = self.driver.title
        return title
        
if __name__ == '__main__':
    am = ActionMethod() 
    am.open_browser('chrome')    
    am.get_url('http://127.0.0.1/zentao/user-login.html')
    am.sleep_time()
    am.element_send_keys('admin', "username")
    am.element_send_keys('Aa1234','password')
    am.sleep_time()
    print(am.get_title())
    am.click_element('submit')
    am.sleep_time()
    am.close_browser()
    
  
  