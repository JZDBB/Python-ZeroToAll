# this is about basis knowledge of web crawler

## part1, url
# import urllib2
#
# url = 'http://www.baidu.com'
#
# # 1
# print 'first method'
# # directly request
# response1 = urllib2.urlopen(url)
# # get the status, if it is 200 that means sucess
# print response1.getcode()
# # read message
# cont = response1.read()
# print len(cont)
#
# # 2
# print 'second method'
# # build a Request Object
# request = urllib2.Request(url)
# # add data
# request.add_data('a')
# # add http header
# request.add_header('User-Agent', 'Mozilla/5.0')
# # send the result of this request
# response2 = urllib2.urlopen(request)
# # get the status, if it is 200 that means sucess
# print response2.getcode()
# # read message
# cont = response2.read()
# print len(cont)
#
# # 3
# print 'third method'
# import cookielib
# # build a cookie vesse l
# cj = cookielib.CookieJar()
# # build a opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
# # install opener
# urllib2.install_opener(opener)
# # use the urllib2 with cookie to call web
# response3 = urllib2.urlopen("http://www.baidu.com/")
# # get the status, if it is 200 that means sucess
# print response3.getcode()
# # read message
# print cj
# cont = response3.read()
# print len(cont)
#
# # problem: urllib2.HTTPError: HTTP Error 503: Service Unavailable
# # answer: refresh is avaliable


# part2, html parser
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# build BeautifulSoup Object according to Html page string
soup = BeautifulSoup(
    html_doc, # Html document string
    'html.parser', # Html parser
    from_encoding='utf8' # Html document encode
)

# # method find_all(name, attrs, string)
# # find all tab about 'a'
# soup.find_all('a')
# # find all tab about 'a' also find node like the form '/view/123.htm'
# soup.find_all('a', href='/view/123.htm')
# soup.find_all('a', href=re.compile(r'/view/d+\.htm'))
# #find all node whose tab is div, class is abc and letters is python
# soup.find_all('div', class_='abc',string='Python')
# when get a node: <a href='1.html'>Python</a>
# use "node.name" to get the name of the tab
# use "node['href']" to get the href
# use "node.get_text()" to get the letters

print 'get all links'
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print 'get the links of lacie'
link_node = soup.find('a', href='http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

print "zhengzhe match"
link_node = soup.find('a', href=re.compile(r"ill"))
print link_node.name, link_node['href'], link_node.get_text()

print 'get p paragraph'
p_node = soup.find('p', class_="title")
print p_node.name, p_node.get_text()
