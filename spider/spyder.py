
import urllib.request
from urllib.parse import quote
import re
info = dict()

import ssl  #导入Python SSL处理模块
#如果网站的SSL证书是经过CA认证，就需要单独处理SSL证书，让程序忽略SSL证书验证错误，即可正常访问


def get_company_info(search_url):
    context = ssl._create_unverified_context() #忽略安全
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }

    # key_word = '上海建发致新医疗供应链管理集团股份有限公司'

    #url="https://www.qcc.com/firm/c19ffeab8bff6a23afb7bc8521c33139.html"


    request=urllib.request.Request(search_url,headers=headers)

    #Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    #在urlopen()方法里 指明添加 context 参数
    response=urllib.request.urlopen(request,context=context).read()
    # print(response.decode('utf-8'))


    # 寻找法人
    rawPattern_faren = r'class="tb">法定代表人</td>.*target="_blank">(.*)</a></span> <!----> <a class="war-link">关联'

    pattern_faren = re.compile(rawPattern_faren, re.MULTILINE)

    searchTxt = response.decode('utf-8')

    with open('./test.txt', 'w') as file:
        file.write(searchTxt)

    match = pattern_faren.findall(response.decode('utf-8'))

    try:
        info['法人'] = match[0]
    except:
        print('没有找到法人')

    

    # 企业类型

    pattern_cType = re.compile(r'企业类型</td> <td>(.*)</td> <td class="tb">', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    try:
        info['企业类型'] = match[0]
    except:
        print('没有找到企业类型')


    # 董事

    # 限定搜索范围

    # sub_search_pattern = re.compile(r'.*<h3 class="title">对外投资</h3>', re.MULTILINE)
    # sub_search_area = sub_search_pattern.findall(response.decode('utf-8'))

    # print(sub_search_area)

    # 搜索董事
    pattern_cType = re.compile(r'<td style="text-align:left;"><div class="td-coy"><span class="headimg"><span class="app-auto-logo" style="width:40px;height:40px;"><span style="font-size:18px;line-height:39px;width:40px;height:40px;border-radius:4px;background-color:#E79177;">.*</span></span></span> <span class="cont"><span class="name"><a href=".*" target="_blank">(.*?)</a></span>.*<span>.*董事.*</span></td><td>', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    info['董事'] = match

    # 监事

    pattern_cType = re.compile(r'<td style="text-align:left;"><div class="td-coy"><span class="headimg"><span class="app-auto-logo" style="width:40px;height:40px;"><span style="font-size:18px;line-height:39px;width:40px;height:40px;border-radius:4px;background-color:#E79177;">.*</span></span></span> <span class="cont"><span class="name"><a href=".*" target="_blank">(.*?)</a></span>.*<span>监事.*</span></td><td>', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    info['监事'] = match

    #财务负责人

    pattern_cType = re.compile(r'<td style="text-align:left;"><div class="td-coy"><span class="headimg"><span class="app-auto-logo" style="width:40px;height:40px;"><span style="font-size:18px;line-height:39px;width:40px;height:40px;border-radius:4px;background-color:#E79177;">.*</span></span></span> <span class="cont"><span class="name"><a href=".*" target="_blank">(.*?)</a></span>.*<span>财务负责人.*</span></td><td>', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))


    if len(match) > 0:
        info['财务负责人'] = match[0]

    # 统一信用代码

    pattern_cType = re.compile(r'''</a></span> <span class="f">
                  统一社会信用代码：
                  <span class="val">
                    (.*)
                  </span></span></div> <div class="rline"><span class="f ca">''', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info['统一信用代码'] = match[0]

    # 成立日期

    pattern_cType = re.compile(r'''<td width="13%" class="tb">成立日期</td> <td width="20%">(.*)</td></tr> <tr><td class="tb">注册资本</td>''', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info['成立日期'] = match[0]

    print(info)
    return info







