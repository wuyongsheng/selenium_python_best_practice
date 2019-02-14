'''
Created on 2019年2月9日

@author: Administrator
'''
from util.read_ini import Read_Ini
from lib2to3.tests.support import driver
from selenium.webdriver.android.webdriver import WebDriver
from selenium import webdriver
from asyncio.tasks import sleep

class FindElement(object):
    
    def __init__(self,driver):
        self.driver = driver
        
    def get_Element(self,key):
        
        read_ini = Read_Ini()
        
        data = read_ini.get_value(key)
        by,value = data.split('>')
        
        try :
            if by == 'id':
                return  self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'css':
                return self.driver.find_elements_by_css_selector(value)[0]
            else:
                return self.driver.find_element_by_tag_name(value)
        except Exception as e:
            print("find_element错误信息：",e)
            return None

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     fd = FindElement(driver)
#     driver.get('http://127.0.0.1/zentao/user-login.html')
#     fd.get_Element('username').send_keys('admin')
#     fd.get_Element('password').send_keys('1233424888')
#     driver.quit()

        