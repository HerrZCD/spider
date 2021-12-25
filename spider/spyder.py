
from constant import *
from os import error
from urllib.parse import quote
import re
# Import ssl to make the program ignore the error of ssl
# certificate's validation
import ssl
import urllib.request

info = dict()

def GetCompanyInfo(search_url):

    context = ssl._create_unverified_context()
    request=urllib.request.Request(search_url, headers=HEADERS)
    response=urllib.request.urlopen(request, context=context).read()

    searchTxt = response.decode('utf-8')
    with open('./test.txt', 'w') as file:
        file.write(searchTxt)

    # search for artificial person
    pattern_faren = re.compile(REGEX_ARTIFICIAL_PERSON, re.MULTILINE)
    match = pattern_faren.findall(searchTxt)

    if len(match) > 0:
        info[STRING_ARTIFICIAL_PERSON] = match[0]
    else:
        error(STRING_NO_ARTIFICIAL_PERSON)

    # search for company type

    pattern_cType = re.compile(REGEX_COMPANY_TYPE, re.MULTILINE)
    match = pattern_cType.findall(response.decode('utf-8'))

    try:
        info[STRING_COMPANY_TYPE] = match[0]
    except:
        error(STRING_NO_COMPANY_TYPE)

    # search for general manager
    pattern_cType = re.compile(REGEX_GENERAL_MANAGER, re.MULTILINE)
    match = pattern_cType.findall(response.decode('utf-8'))
    if len(match) > 0:
        info[STRING_GENERAL_MANAGER] = match
    else:
        error(STRING_NO_GENERAL_MANAGER)

    # search for supervisor

    pattern_cType = re.compile(REGEX_SUPERVISOR, re.MULTILINE)
    match = pattern_cType.findall(response.decode('utf-8'))
    if len(match) > 0:
        info[STRING_SUPERVISOR] = match
    else:
        error(STRING_NO_SUPERVISOR)

    # search for finacial manager

    pattern_cType = re.compile(REGEX_FINACIAL_MANAGER, re.MULTILINE)
    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info[STRING_FINACIAL_MANAGER] = match[0]
    else:
        error(STRING_NO_FINACIAL_MANAGER)

    # search for union social credit code

    pattern_cType = re.compile(REGEX_CREDIT_CODE, re.MULTILINE)
    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info[STRING_CREDIT_CODE] = match[0]
    else:
        error(STRING_NO_CREDIT_CODE)


    # search for establish time

    pattern_cType = re.compile(REGEX_ESTABLISH_TIME, re.MULTILINE)
    match = pattern_cType.findall(response.decode('utf-8'))

    if len(match) > 0:
        info[STRING_ESTABLISH_TIME] = match[0]
    else:
        error(STRING_NO_ESTABLISH_TIME)

    return info
