# -*- coding: utf-8 -*-

from urllib import urlretrieve
from bs4 import BeautifulSoup
import random
import codecs
import xlwt
from hashlib import md5
import fact_triple_extraction1chen
import re
from postData import *
from datetime import datetime, timedelta
# import db_connect
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%a, %d %b %Y %H:%M:%S",
                    filename="myapp.log",
                    filemode="w")

hosturl = "http://192.168.128.82:8080/Sk/News/data"


class Crawl_web():
    def __init__(self, timeFrame=0, saveFile=True):
        self.saveFile = saveFile
        self.deadlineTime = 0
        self.index = 0
        self.titles = []
        if timeFrame == 0:
            self.deadlineTime = 0
        else:
            self.deadlineTime = (datetime.now() - timedelta(days=timeFrame)).strftime("%Y-%m-%d")
        self.my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]
        # self.starturl = "http://so.news.cn/getNews?keyword=%E6%81%90%E6%80%96%E8%A2%AD%E5%87%BB&curPage=1&sortField=0&searchFields=1&lang=cn"
        # self.starturl = "https://cn.nytimes.com/search?query=%E6%81%90%E6%80%96&lang=&dt=json&from=0&size=10"
        # self.starturl = "https://www.wsj.com/search/term.html?KEYWORDS=terrorist"
        self.starturl = "http://search.chinadaily.com.cn/all_cn.jsp?searchText=%E6%81%90%E6%80%96%E8%A2%AD%E5%87%BB"  # 法国

    def get_page_count(self, url, headers):
        '''
        获取新华网中，该关键词的总页面信息
        '''
        print "起始url是：" + url
        html = None

        html = self.getUrl_multiTry(url, headers)
        # 对获取到的文本进行解析
        soup = BeautifulSoup(html, 'lxml')
        # 从解析文件中通过select选择器定位指定的元素，返回一个列表
        result_count = soup.select("ul.list > p.search-summary-results")
        result_count = result_count[0].encode('gbk')
        result_count = filter(str.isdigit, result_count)
        print 'result_count--------', result_count

        page_count = soup.select("ol.pagination-search")
        page_count = str(page_count).split('%5D=')[-1]
        page_count = page_count.split('"')[0]
        # page_count = re.findall(r"\d+\.?\d*",str(page_count))
        print 'page_count--------', page_count
        pacgeCount = int(page_count)
        resultCount = int(result_count)

        return pacgeCount, resultCount

    def index_info(self,url,headers):
        '''
        获取一个页面中的所有的条目相关信息:
        页面中所有条目的标题、关键词、报道时间、报道内容以及图片链接
        '''
        print "当前页面的url是：" + url
        #返回的结果数组，为每个新闻的一些简略信息，包括title、des、url等
        result = []
        #爬虫获取url结果

        html=self.getUrl_multiTry(url,headers)

        #解析返回的json结果
        content_dict = json.loads(html)
        if content_dict.has_key("content") and content_dict["content"].has_key("results") and content_dict["content"].has_key("results")!=None:
            for i in content_dict["content"]["results"]:



                #title=普京称圣彼得堡超市爆炸是<font color=red>恐怖袭击</font>
                #去除title的html样式
                titleStr = "".join(i["title"])
                soup = BeautifulSoup(titleStr, 'html.parser', from_encoding='utf-8')
                titleStr = soup.get_text()
                if titleStr  in self.titles:
                    continue
                self.titles.append(titleStr)
                index_result={}
                index_result["title"]=titleStr
                index_result["imgUrl"]=i["imgUrl"]
                index_result["keyword"]=i["keyword"]
                index_result["sitename"]=i["sitename"]
                index_result["url"]=i["url"]
                index_result["reporttime"]="".join(i["pubtime"])
                index_result["content"]=""

                if(i["des"]!=None):
                    des= "".join(i["des"])
                    soup = BeautifulSoup(des, 'html.parser', from_encoding='utf-8')
                    des = soup.get_text()
                    index_result["des"]=des
                else:
                    index_result["des"]=""
                result.append(index_result)
        return result

    def start_crawl(self):
        '''
        这个函数开始爬取数据
        '''
        # 获取到页面和条目统计信息
        fileName = ''
        stopFlag = False
        CrawlData = {}
        # FilterData={}
        # pages, indexcount = self.get_page_count(self.starturl, self.my_headers)
        pages, indexcount =  2275, 22757
        fields = ["reporttime", "reporter", "title", "sitename", "keyword", "content", "imgUrl"]
        # 根据是否需要记录文件来进行
        EventInfoExtract = fact_triple_extraction1chen.EventInfoExtract(r"3.3.0\ltp_data", 'out123.txt')
        index = 0
        # 遍历所有的新闻页
        for i in range(1, pages + 1):
            # 得到当前页的url
            urls = self.starturl.replace("curPage=1", "curPage=%d" % i)
            # 返回数组对象，每个元素表示一条新闻的简略信息
            infodexs = self.index_info(urls, self.my_headers)
            if len(infodexs) > 0:
                for infodex in infodexs:
                    # 判断是否达到终止天数
                    if self.deadlineTime != 0 and infodex["reporttime"][0:10] < self.deadlineTime:  # 终止爬取
                        stopFlag = True
                        if (EventInfoExtract.segmentor != None):
                            EventInfoExtract.release_module()
                        break
                    if (infodex["keyword"] == "视频"):
                        continue
                    print "=====================新闻信息=========================="
                    print infodex["url"]
                    body = self.get_news_body(infodex["url"], self.my_headers)
                    if body != None:
                        infodex["content"] = body["content"]
                        infodex["reporter"] = u"新华社"
                    index += 1
                    # 恢复为原来的段落
                    datas = infodex["content"].split(u"　　")
                    EventInfoExtract.InitModule()

                    # print '数据-----------------', datas
                    for data in datas:
                        print data.encode("utf-8")

                        if len(data.encode("utf-8")) < 30 or data.encode("utf-8") == None:
                            continue
                        TimeAndAddress = EventInfoExtract.addresssTime_extract(data.encode("utf-8"))
                        # print TimeAndAddress
                        fact_attribute = EventInfoExtract.fact_attribute_from_text(data.encode("utf-8"))
                        orgnization = EventInfoExtract.organization_from_text(data.encode("utf-8"))
                        death_num, hurt_num, total_num = EventInfoExtract.death_num_from_text(data.encode("utf-8"))
                        if TimeAndAddress[0]["date"] == "" and TimeAndAddress[0]["address"] == "":
                            continue
                        print '''
    时间\t地点\t事件类型\t攻击组织\t伤亡总人数\t死亡人数\t受伤人数
    %s--%s--%s--%s--%s--%s--%s''' % (
                        TimeAndAddress[0]['date'], TimeAndAddress[0]['address'], fact_attribute, orgnization, total_num,
                        death_num, hurt_num)
                    # print("start to releases")

                    # 将新闻的原文也进行保存

                    imgUrl = infodex["imgUrl"]
                    imgName = ""
                    if (imgUrl != None and imgUrl != ""):
                        imgName = imgUrl.split("/")[-1]
                        urlretrieve("http://tpic.home.news.cn/xhCloudNewsPic/" + imgUrl, "./imgs/" + imgName)
                    print infodex
                    news = {}
                    news["title"] = infodex["title"]
                    news["des"] = infodex["des"]
                    news["pubtime"] = infodex["reporttime"]
                    news["content"] = infodex["content"]
                    news["img"] = imgName
                    news["url"] = infodex["url"]

                    news['time'] = TimeAndAddress[0]['date']
                    news['address'] = TimeAndAddress[0]['address']
                    news['type'] = fact_attribute

                    if (total_num != None):
                        news['total'] = "伤亡:" + total_num
                    else:
                        if death_num == None:
                            death_num = "0"
                        if hurt_num == None:
                            hurt_num = "0"
                        # print death_num, hurt_num
                        news['total'] = "死亡：" + death_num + "，受伤：" + hurt_num
                    news["gname"] = orgnization
                    news['nwound'] = hurt_num
                    news['nkill'] = death_num

                    # insertSql = db_connect.generateSQL(news)
                    # print insertSql
                    # db_connect.insertOneData(insertSql)


                    # PostData(data,hosturl)
                    EventInfoExtract.release_module()

                if stopFlag == True:
                    print "sTOPP ING"
                    break
        if (EventInfoExtract.segmentor != None):
            EventInfoExtract.release_module()
        sys.exit(0)
        print "Here Release-=======--==="

    def getUrl_multiTry(self,url,headers):
        time.sleep(1)
        maxTryNum = 10
        for tries in range(maxTryNum):
            try:
                randddom_header = random.choice(headers)
                req = urllib2.Request(url)
                req.add_header("User-Agent", randddom_header)
                req.add_header("GET", url)
                html = urllib2.urlopen(req).read().decode(encoding="utf8", errors='ignore')
                return html
            except:
                if tries < (maxTryNum - 1):
                    continue
                else:
                    logging.error("Has tried %d times to access url %s, all failed!", maxTryNum, url)
                    break




#获取新闻的标题和链接
if __name__=="__main__":
    #print "hello world"
    xinhuaCrawl = Crawl_web(timeFrame=0,saveFile=True)
    xinhuaCrawl.start_crawl()
    # db_connect.close()
    '''
    EventInfoExtract = fact_triple_extraction1chen.EventInfoExtract(r"F:\ltp_data_v3.4.0",'out123.txt')
    EventInfoExtract.InitModule()
    data = "２０１４年１２月１６日，一伙装扮成军人的武装人员袭击了白沙瓦一所军人子弟学校，造成１５０人死亡，死者绝大多数为学生。巴基斯坦塔利班宣称制造了这一袭击事件。（包雪琳）（新华社专特稿）"
    dt=EventInfoExtract.addresssTime_extract(data)
    print dt[0]['address']
    print dt[0]['date']
    EventInfoExtract.release_module()
    '''
