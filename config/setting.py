'''
Created on 2019年2月9日

@author: Administrator
'''
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
report_dir = os.path.join(base_dir,"report")
config_ini = os.path.join(base_dir,"config","LocateElement.ini")
excel_default_path = os.path.join(base_dir,'ex_data','casedata.xlsx')
excel_keyword_path = os.path.join(base_dir,'ex_data','keyword.xlsx')


if __name__ == '__main__':
    print(config_ini)
    print(report_dir)
    print(excel_keyword_path)
    print(excel_default_path)
