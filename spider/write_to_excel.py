from xlutils.copy import copy
import xlwt,xlrd
from constant import *


def WriteToExcel(company_info,search_keyword,index):
    data = xlrd.open_workbook('modal.xls',formatting_info=True)
    excel = copy(wb=data)
    excel_table = excel.get_sheet(0)
    table = data.sheets()[0]
    excel_table.write(index,1,company_info[STRING_COMPANY_TYPE])
    excel_table.write(index,2,company_info[STRING_ARTIFICIAL_PERSON])
    excel_table.write(index,9,' '.join(company_info[STRING_GENERAL_MANAGER]))
    excel_table.write(index,10,' '.join(company_info[STRING_SUPERVISOR]))
    excel_table.write(index,13,company_info[STRING_ESTABLISH_TIME])

    excel_table.write(index,12,company_info[STRING_CREDIT_CODE])
    excel_table.write(index,3,search_keyword)
    excel_table.write(index,0,index)
    excel.save('modal.xls')
