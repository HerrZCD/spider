
import requests
from lxml import etree
import random
import re
#目标采集地址
base_url1='http://m.qichacha.com'
base_url='https://m.qichacha.com/search?key='

user_agent=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
]
cookie=[
'UM_distinctid=16518280d1e3e5-00788a93df88f7-5b193413-1fa400-16518280d1f949; zg_did=%7B%22did%22%3A%20%2216518280dd3b45-0da4e4ab13f793-5b193413-1fa400-16518280dd51f6%22%7D; acw_tc=7b81f49815356947470295339e1fc37a590000ea6190b3cf75ab42853b; PHPSESSID=4l787fmr2v90mh2khj8n6n64l5; CNZZDATA1254842228=226405416-1535690886-null%7C1535690886; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1535595956,1535618789,1535618810,1535694746; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201535694746927%2C%22updated%22%3A%201535695379242%2C%22info%22%3A%201535595953976%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22m.baidu.com%22%2C%22cuid%22%3A%20%227d775544e16a1cc0d0ab63b42b4b8aef%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1535695379',
'UM_distinctid=16518280d1e3e5-00788a93df88f7-5b193413-1fa400-16518280d1f949; zg_did=%7B%22did%22%3A%20%2216518280dd3b45-0da4e4ab13f793-5b193413-1fa400-16518280dd51f6%22%7D; acw_tc=7b81f49815356947470295339e1fc37a590000ea6190b3cf75ab42853b; PHPSESSID=4l787fmr2v90mh2khj8n6n64l5; CNZZDATA1254842228=226405416-1535690886-null%7C1535690886; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1535595956,1535618789,1535618810,1535694746; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201535694746927%2C%22updated%22%3A%201535695791508%2C%22info%22%3A%201535595953976%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22m.baidu.com%22%2C%22cuid%22%3A%20%227d775544e16a1cc0d0ab63b42b4b8aef%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1535695792',
'UM_distinctid=16518280d1e3e5-00788a93df88f7-5b193413-1fa400-16518280d1f949; zg_did=%7B%22did%22%3A%20%2216518280dd3b45-0da4e4ab13f793-5b193413-1fa400-16518280dd51f6%22%7D; acw_tc=7b81f49815356947470295339e1fc37a590000ea6190b3cf75ab42853b; PHPSESSID=4l787fmr2v90mh2khj8n6n64l5; CNZZDATA1254842228=226405416-1535690886-null%7C1535690886; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1535595956,1535618789,1535618810,1535694746; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201535694746927%2C%22updated%22%3A%201535695924595%2C%22info%22%3A%201535595953976%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22m.baidu.com%22%2C%22cuid%22%3A%20%227d775544e16a1cc0d0ab63b42b4b8aef%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1535695925',
'UM_distinctid=16518280d1e3e5-00788a93df88f7-5b193413-1fa400-16518280d1f949; zg_did=%7B%22did%22%3A%20%2216518280dd3b45-0da4e4ab13f793-5b193413-1fa400-16518280dd51f6%22%7D; acw_tc=7b81f49815356947470295339e1fc37a590000ea6190b3cf75ab42853b; PHPSESSID=4l787fmr2v90mh2khj8n6n64l5; CNZZDATA1254842228=226405416-1535690886-null%7C1535690886; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1535595956,1535618789,1535618810,1535694746; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201535694746927%2C%22updated%22%3A%201535696003819%2C%22info%22%3A%201535595953976%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22m.baidu.com%22%2C%22cuid%22%3A%20%227d775544e16a1cc0d0ab63b42b4b8aef%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1535696005'
]
# 请求头设置
headers={
    'User-agent': random.choice(user_agent),
    'cookie': random.choice(cookie)
}

name_list=['成都创信广告有限公司']

for name in name_list:
    start_url=base_url+str(name)
    print(start_url)
    response = requests.get(start_url, headers=headers)
    _response=response.text
    # print(_response)
    # content = etree.HTML(_response)
    # print(content)
    #获取筛选信息链接
    search_url=re.findall('</div> <a href="(.*?)" class="a-decoration"> <div class="list-item"> <div class="list-item-top">',_response)
    url=base_url1+search_url[0]
    # print(url)
    # print('*'*100)
    response1 = requests.get(url,headers=headers)
    _response1=response1.text
    #公司名称
    company_name=re.findall('<div class="company-name">(.*?)<',_response1)[0]
    print('公司名称:'+company_name)
    #法人
    legal_person=re.findall('<a class="oper" href=".*?">(.*?)</a>',_response1)[0]
    print('法人:'+legal_person)
    #电话
    telephone=re.findall('<a href="tel:.*?" class="phone a-decoration">(.*?)</a>',_response1)[0]
    print('电话:'+telephone)
    # #地址
    # address=re.findall('</div> <div class="address">(.*?)</div> </div>',_response1)[0]
    # print(address)
    # # print('地址:'+address)

    # #注册号
    # registration_number=re.findall('</div><div class="basic-item-right">(.*?)</div>',_response1)
    # print(registration_number)
