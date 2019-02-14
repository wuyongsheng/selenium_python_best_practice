'''
Created on 2019年2月12日

@author: Administrator
'''
from util.excel_cell_value import Get_Cell_Value
from util.actionMethod import ActionMethod
from config import setting
from log.log_base import UserLog


class KeywordCase(object):
    def  __init__(self):
        self.action_method = ActionMethod()
        excel_default_path = setting.excel_keyword_path
        self.get_cell_value = Get_Cell_Value(excel_default_path)
        user = UserLog()
        self.log = user.get_log()
        
    def run_main(self):
        get_lines = self.get_cell_value.get_lines
        if get_lines:
            for i in range(1,get_lines):
                is_run = self.get_cell_value.get_is_run(i)
                if is_run == 'yes':
                    print('执行到第{}行'.format(i))
                    carry_method = self.get_cell_value.get_action_method(i)
                    send_value = self.get_cell_value.get_send_value(i)
                    oper_element = self.get_cell_value.get_oper_element(i)
                    expect_result_method = self.get_cell_value.get_expect_result(i)
                    real_result_value = self.get_cell_value.get_real_result(i)
                    self.run_method(carry_method,send_value,oper_element)
                    
                    if expect_result_method != '':
                        result_value = self.get_real_result_value(real_result_value)
                        if result_value[0] == 'text':
                            result = self.run_method(expect_result_method)
                            if result_value[1] in result:
                                self.get_cell_value.write_cell_value(i, 'pass')
                            else:
                                self.get_cell_value.write_cell_value(i, 'fail')
                        elif result_value[0] == 'element':
                            result = self.run_method(expect_result_method, result_value[1])
                            if result :
                                self.get_cell_value.write_cell_value(i, 'pass')
                            else:
                                self.get_cell_value.write_cell_value(i, 'fail')
                        else:
                            print("Error:实际要求结果：{},厕所无效".format(real_result_value))
                    else:
                        print('预期结果为空')
                            
                    
    def run_method(self,method,send_value = '',handle_value = ''):
        main_method = getattr(self.action_method, method)  
        print(main_method)
        if send_value == '' and handle_value == '':
            self.log.error('no send value ,no handle value !')
            result = main_method()
            return result
        elif send_value == '' and handle_value != '':
            result = main_method(handle_value)
        elif send_value != '' and handle_value == '':
            result = main_method(send_value)
        else:
            result = main_method(send_value,handle_value)
            
    def get_real_result_value(self,data):
        self.log.info('get real result !')
        return data.split('=')
        
            
if __name__ == '__main__':
    keyword_case = KeywordCase()
    keyword_case.run_main()
    
    
    
    
    
    
                    