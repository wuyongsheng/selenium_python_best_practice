'''
Created on 2019年2月13日

@author: Administrator
'''
import logging
import os
import datetime


class UserLog(object):

    def __init__(self):
        self.logger1 = logging.getLogger(__name__)  # 生成log对象
        # 以下三行代码为清空上次创建log文件
        logging.Logger.manager.loggerDict.pop(__name__)  # 清空当前文件存于loggerDict的日志实例。(logging 模块为了保证同一个名称引用同一个日志实例,所以就把所有的日志实例全部存在了一个 loggerDict 的字典里，要释放某实例则需清除)
        self.logger1.handlers=[]  # 将handers清空
        self.logger1.removeHandler(self.logger1.handlers) # 移除当前文件的logging相关配置
        if not self.logger1.handlers:  # 如果logger.handlers列表为空，则新添加，否则表示文件存在，可以直接去写日志

            self.logger1.setLevel(logging.DEBUG)
            #控制台输出日志
            #consle = logging.StreamHandler()
            #logger.addHandler(consle)

            #文件名字
            log_dir = os.path.dirname(os.path.abspath(__file__))
            log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
            log_name = os.path.join(log_dir,"logs",log_file) # 日志文件名
            #文件输出日志
            self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
            self.file_handle.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
            self.file_handle.setFormatter(formatter)
            self.logger1.addHandler(self.file_handle)


    def get_log(self):
        return self.logger1
    
    def close_handle(self):
        self.logger1.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.info('test')
    user.close_handle()