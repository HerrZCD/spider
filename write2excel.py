
import xlwt,xlrd
from xlutils.copy import copy
def write2excel(company_info,search_keyword,index):
    data = xlrd.open_workbook('modal.xls',formatting_info=True)
    excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0) # 获得要操作的页
    table = data.sheets()[0]
    excel_table.write(index,1,company_info['企业类型'])
    excel_table.write(index,2,company_info['法人'])
    excel_table.write(index,9,' '.join(company_info['董事']))
    excel_table.write(index,10,' '.join(company_info['监事']))
    excel_table.write(index,13,company_info['成立日期'])

    excel_table.write(index,12,company_info['统一信用代码'])
    excel_table.write(index,3,search_keyword)   # 公司名
    excel_table.write(index,0,index)   # 序号
    excel_table.write(index,16,company_info['住所'])   # 住所



    # nrows = table.nrows # 获得行数
    # ncols = table.ncols # 获得列数
    # values = ["E","X","C","E","L"] # 需要写入的值
    # for value in values:
    #     excel_table.write(nrows,1,value) # 因为单元格从0开始算，所以row不需要加一
    #     nrows = nrows+1
    excel.save('modal.xls')
