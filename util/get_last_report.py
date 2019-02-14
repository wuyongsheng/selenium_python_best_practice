'''
Created on 2019年2月9日

@author: Administrator
'''
import os
from config import setting

class Get_Latest_Report(object):
    
    def latest_file(self):
        file_lists = os.listdir(setting.report_dir)
#         print(file_lists)
        
        latest_report_file = self.get_latest_report_file(file_lists)
        return latest_report_file
    
    def get_latest_report_file(self,lists):
        report_list = []
        for l in lists :
            if l.endswith('html'):
                report_list.append(l)
                
        latest_report = report_list[-1]
        
        return latest_report

if __name__ == '__main__':
    g = Get_Latest_Report()
    print(g.latest_file())
        