# /usr/bin/env python
# coding=utf8
import urllib
import urllib2
import cookielib
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def PostData(data,host):
    #hosturl = 'http://localhost:8080/Sk/News/data'
    hosturl=host
    postdata=data
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    try:
        # cookie set
        # 用来保持会话
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        # encode postdata
        enpostdata = urllib.urlencode(postdata)
        # request url
        urlrequest = urllib2.Request(hosturl, enpostdata, headers)
        # open url
        urlresponse = urllib2.urlopen(urlrequest)
        # return url
        result = urlresponse.read()
        print result
    except Exception, e:
        # print e
        return -164282925

    # response = requests.post(url, data, headers=headers)
    # head = response.headers

    # text = response.text
    # text = json.loads(text)
    # res = text['trans_result']['data'][0]['dst']
    # print(res)
    # print(head['Content-Type'])
    # print response.json()


if __name__ == "__main__":
    # translate()
    pass
