from lxml import etree
from spyder import GetCompanyInfo
from write_to_excel import WriteToExcel
import requests
import re

companies = ['西安致康医疗供应链管理有限公司', '米哈游', '微软中国']

class QCC(object):
    def __init__(self):
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }

    def GetCookie(self):
        url = 'https://www.qcc.com/web/search?key=测试'
        response = requests.get(url, headers=self._headers, allow_redirects=False)
        response.encoding = 'utf8'
        result = re.findall(r'div>您的请求ID是: <strong>\n(.*?)</strong></div>',  response.text)
        if result:
            return result[0]

    def Search(self, search_keyword,index):
        url = 'https://www.qcc.com/web/search?key={}'.format(search_keyword)
        headers = self._headers
        headers['cookie'] = 'acw_tc={}'.format(self.GetCookie())
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        html = etree.HTML(response.text)
        com_url = html.xpath('//a[@class="title copy-value"]/@href')
        for url in com_url:
            company_info = GetCompanyInfo(url)
            WriteToExcel(company_info,search_keyword,index)
            return

    def Run(self):
        index = 1
        for i in range(len(companies)):
            self.Search(search_keyword=companies[i], index=index)
            index += 1


if __name__ == '__main__':
    t = QCC()
    t.Run()
