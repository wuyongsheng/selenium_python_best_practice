# selenium_python_best_practice
selenium python 最佳实践（参考了网上的各种案例，基于禅道系统）
>  春节回去后，利用空余时间写了一下 selenium python 的代码，参考了CSDN 和博客园中的一些案例，在代码中使用了unittest 单元测试框架，采用了分层的用例设计（包括页面层，页面元素操作层，业务层，用例层），PO模型（页面对象模型），通过读取 ini 配置文件以及Excel，实现数据与代码的分离，同时也实现了数据驱动、关键字驱动测试，此外在代码中还加入了日志模块，将日志记录到日志文件中以便问题的定位。在测试执行结束之后会自动生成测试报告，并能通过邮件将测试报告进行发送。

### 模块功能说明

![模块说明.png](https://upload-images.jianshu.io/upload_images/12273007-3762d82d8118bd3a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###  关键字驱动

![关键字驱动.jpg](https://upload-images.jianshu.io/upload_images/12273007-0aae8b8e6d21258f.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 测试报告

![report.jpg](https://upload-images.jianshu.io/upload_images/12273007-d15d0635b8d69a3b.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 邮件发送

![邮件发送.jpg](https://upload-images.jianshu.io/upload_images/12273007-6199750f1f00ebb8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### github 代码地址

https://github.com/wuyongsheng/selenium_python_best_practice
