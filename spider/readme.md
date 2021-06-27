#### 企查查搜索公司 => 爬取公司信息 => 写入Excel

##### 公司列表设置

*main.py*

line 14

    companies = ['西安致康医疗供应链管理有限公司', '山东致新医疗供应链管理有限公司']

    需要爬取的公司放到这个列表即可

##### 运行

    python3 main.py

结果会输出到**modal.xls**中

##### Preview

![avatar](./images/demo.png)

##### 注意事项

+ Python3中xlutils保存：TypeError: descriptor 'decode' requires a 'bytes' object but received a 'NoneType' [修复方法](https://blog.csdn.net/zhangvalue/article/details/105170305)
+ xlwt不支持对xlsx的操作，所以本项目用的excel模板是个xls，大家想自定义模版的时候请注意

###### contact me

Email：352273172@qq.com

