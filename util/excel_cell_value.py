'''
Created on 2019年2月12日

@author: Administrator
'''
from util.excel_operation import Excel_Operation
import xlrd
from xlutils import copy
import time
from config.setting import excel_keyword_path
from log.log_base import UserLog



class Get_Cell_Value(object):
    def __init__(self,excel_path):
        self.case_id = 0
        self.case_name = 1
        self.action_type = 2
        self.is_run = 3
        self.action_method = 4
        self.send_value = 5
        self.oper_element = 6
        self.expect_result = 7
        self.real_result = 8
        self.report_result = 9
        
        self.excel_path = excel_path
        self.excel_oper = Excel_Operation(self.excel_path) 
        self.get_lines = self.excel_oper.get_lines()
        
        user = UserLog()
        self.log = user.get_log()

        
    def get_case_id(self,row):
        case_id = self.excel_oper.get_col_value(row, self.case_id)
        return case_id
    
    def get_case_name(self,row):
        case_name = self.excel_oper.get_col_value(row, self.case_name)
        return case_name
    
    def get_is_run(self,row):
        is_run = self.excel_oper.get_col_value(row, self.is_run)
        self.log.info('is run ?')
        return is_run
    
    def get_action_method(self,row):
        action_method = self.excel_oper.get_col_value(row, self.action_method)
        return action_method
        
    def get_send_value(self,row):
        send_value = self.excel_oper.get_col_value(row, self.send_value)
        return send_value
        
    def get_oper_element(self,row):
        oper_element = self.excel_oper.get_col_value(row, self.oper_element)
        return oper_element
    
    def get_expect_result(self,row):
        expect_result = self.excel_oper.get_col_value(row, self.expect_result)
        return expect_result
    
    def get_real_result(self,row):
        real_result = self.excel_oper.get_col_value(row, self.real_result) 
        return real_result
    
    def get_report_result(self,row):
        report_result = self.excel_oper.get_col_value(row, self.report_result)
        return report_result

    def write_cell_value(self,row,value):
        self.excel_oper.write_value(row,self.report_result, value)
        
if __name__ == '__main__':
    get_va = Get_Cell_Value(excel_keyword_path)
    print(get_va.get_is_run(5))
    print(get_va.get_report_result(5))
    print(get_va.get_case_name(5))
        
    




















