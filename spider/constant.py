# This file stores constants of regex and browser header,
# Once the html structure of the target website is changed
# we should update the regex.

# regex
REGEX_ARTIFICIAL_PERSON = r'<span class="val"><span class="max-130"><span><a href=".*" target="_blank">(.*)</a></span></span>'

REGEX_COMPANY_TYPE = r'</td> <td>(.*)</td> <td class="tb">营业期限'

REGEX_GENERAL_MANAGER = r'</td> <td class="left"><div class="td-coy"><span class="headimg"><span class="app-auto-logo" style="width:40px;height:40px;"><span style="font-size:18px;line-height:39px;width:40px;height:40px;border-radius:4px;background-color:#E79177;">.*</span></span></span> <span class="cont"><span class="name"><a href=".*" target="_blank">(.*)</a></span>.*</span> <span class="foot"><a class="war-link"><i aria-label="icon.*" class="anticon anticon-icon-icon_guanlianqiye aicon aicon-guanlianqiye"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false"><use xlink:href=".*"></use></svg></i> <span>关联.*家企业 &gt;</span></a></span> </div></td><td><span>.*董事.*</span></td><td class="filter-blur"><div>.*</div></td><td class="filter-blur"><div>.*</div></td></tr> <tr> <td class="tx">'

REGEX_SUPERVISOR = r'<em>姓名: <a href=".*" target="_blank">(.*?)</a>; 证件号码: .*; 职位.*监事.*</em></span>'

REGEX_FINACIAL_MANAGER = r'<em>现</em>财务负责人姓名:<em>(.*)\,.*</em>财务负责人固定电话'

REGEX_CREDIT_CODE = r'''统一社会信用代码：
                  <span class="val"><div class="app-copy-box copy-hover-item" data-v-.*><span class="copy-value" data-v-.*>(.*)</span> <span class="app-copy copy-button-item"'''

REGEX_ESTABLISH_TIME = r'class="tb">成立日期 <i aria-label=".*" class=".*"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false"><use xlink:href=".*"></use></svg></i></td> <td width="20%">(.*)</td></tr> <tr><'

# string macros
STRING_ARTIFICIAL_PERSON = '法人'
STRING_NO_ARTIFICIAL_PERSON = '没有找到法人'
STRING_COMPANY_TYPE = '企业类型'
STRING_NO_COMPANY_TYPE = '没有找到企业类型'
STRING_GENERAL_MANAGER = '董事'
STRING_NO_GENERAL_MANAGER = '没有找到董事'
STRING_SUPERVISOR = '监事'
STRING_NO_SUPERVISOR = '没有找到监事'
STRING_FINACIAL_MANAGER = '财务负责人'
STRING_NO_FINACIAL_MANAGER = '没有找到财务负责人'
STRING_CREDIT_CODE = '统一信用代码'
STRING_NO_CREDIT_CODE = '没有找到统一信用代码'
STRING_ESTABLISH_TIME = '成立日期'
STRING_NO_ESTABLISH_TIME = '没有找到成立日期'

# headers

HEADERS = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}



