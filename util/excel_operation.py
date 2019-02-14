'''
Created on 2019年2月12日

@author: Administrator
'''
import xlrd
from xlutils.copy import copy
import time
from config.setting import excel_keyword_path
from config.setting import excel_default_path

class Excel_Operation(object):
    
    def __init__(self,ex_path = None,index = None):
        if ex_path == None:
            self.excel_path = excel_keyword_path
        else:
            self.excel_path = ex_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
        
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(1,rows):
                row = self.table.row_values(i)
                result.append(row)
            return result
        return None
        
        
    def get_lines(self):
        rows = self.table.nrows
        if rows > 1:
            return rows
        return None
    
    def get_col_value(self,row,col):
        if self.get_lines() > row:
            data = self.table.cell(row,col).value
            return data
        return None
    
    def write_value(self,row,col,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excel_path)
        time.sleep(2)

        
if __name__ == '__main__':
#     ex_oper = Excel_Operation(excel_default_path)
#     ex_data = ex_oper.get_data()
#     print(*ex_data)
    
    ex_op = Excel_Operation()
    le  = ex_op.get_lines()
    print('lines is : ')
    print(le)
    va  = ex_op.get_col_value(5, 9)
    print('value is : '+ va)
    da  = ex_op.get_data()
    print('data is : ')
    print(da)
    ex_op.write_value(5,9, 'huhggf9999')
    va  = ex_op.get_col_value(5, 9)
    print('value is : '+ va)