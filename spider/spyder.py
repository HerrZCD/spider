
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

    print(search_url)


    request=urllib.request.Request(search_url,headers=headers)

    #Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    #在urlopen()方法里 指明添加 context 参数
    response=urllib.request.urlopen(request,context=context).read()
    #  print(response.decode('utf-8'))


    # 寻找法人
    rawPattern_faren = r'<span class="val"><span class="max-130"><span><a href=".*" target="_blank">(.*)</a></span></span>'

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

    pattern_cType = re.compile(r'</td> <td>(.*)</td> <td class="tb">营业期限', re.MULTILINE)

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
    pattern_cType = re.compile(r'</td> <td class="left"><div class="td-coy"><span class="headimg"><span class="app-auto-logo" style="width:40px;height:40px;"><span style="font-size:18px;line-height:39px;width:40px;height:40px;border-radius:4px;background-color:#E79177;">.*</span></span></span> <span class="cont"><span class="name"><a href=".*" target="_blank">(.*)</a></span>.*</span> <span class="foot"><a class="war-link"><i aria-label="icon.*" class="anticon anticon-icon-icon_guanlianqiye aicon aicon-guanlianqiye"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false"><use xlink:href=".*"></use></svg></i> <span>关联.*家企业 &gt;</span></a></span> </div></td><td><span>.*董事.*</span></td><td class="filter-blur"><div>.*</div></td><td class="filter-blur"><div>.*</div></td></tr> <tr> <td class="tx">', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    info['董事'] = match

    # 监事

    pattern_cType = re.compile(r'<em>姓名: <a href=".*" target="_blank">(.*?)</a>; 证件号码: .*; 职位.*监事.*</em></span>', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    info['监事'] = match

    #财务负责人

    pattern_cType = re.compile(r'<em>现</em>财务负责人姓名:<em>(.*)\,.*</em>财务负责人固定电话', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))


    if len(match) > 0:
        info['财务负责人'] = match[0]

    # 统一信用代码

    pattern_cType = re.compile(r'''统一社会信用代码：
                  <span class="val"><div class="app-copy-box copy-hover-item" data-v-.*><span class="copy-value" data-v-.*>(.*)</span> <span class="app-copy copy-button-item"''', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info['统一信用代码'] = match[0]

    print(match, '------')

    # 成立日期

    pattern_cType = re.compile(r'class="tb">成立日期 <i aria-label=".*" class=".*"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false"><use xlink:href=".*"></use></svg></i></td> <td width="20%">(.*)</td></tr> <tr><', re.MULTILINE)

    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info['成立日期'] = match[0]

    print(info)
    return info







