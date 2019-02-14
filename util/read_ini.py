'''
Created on 2019年2月9日

@author: Administrator
'''
from config.setting import  config_ini
import configparser
from hamcrest.core.core.isnone import none

class Read_Ini(object):
    '''读取配置文件信息'''
    def __init__(self, sec = None):
        if sec :
            self.sec = sec
        else :
            self.sec = 'LoginElement'
            
        self.cf = configparser.ConfigParser()
        self.cf.read(config_ini)
    
    def get_value(self,key):
        data = self.cf.get(self.sec, key)
        return data
    
# if __name__ == '__main__':
# #     print(config_ini)
#     read_init = Read_Ini()
#     print(read_init.get_value('username'))
       