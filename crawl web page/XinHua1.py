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
#import db_connect
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                datefmt="%a, %d %b %Y %H:%M:%S",
                filename="myapp.log",
                filemode="w")

hosturl = "http://192.168.128.82:8080/Sk/News/data"
class Crawl_Xinhua():
    def __init__(self,timeFrame=0,saveFile=True):
        self.saveFile = saveFile
        self.deadlineTime = 0
        self.index=0
        self.titles=[]
        if timeFrame==0:
            self.deadlineTime=0
        else:
            self.deadlineTime=(datetime.now()-timedelta(days=timeFrame)).strftime("%Y-%m-%d")
        self.my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14", 
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  ] 
        #self.starturl = "http://so.news.cn/getNews?keyword=%E6%81%90%E6%80%96%E8%A2%AD%E5%87%BB&curPage=1&sortField=0&searchFields=1&lang=cn"
        #self.starturl = "https://cn.nytimes.com/search?query=%E6%81%90%E6%80%96&lang=&dt=json&from=0&size=10"
        #self.starturl = "https://www.wsj.com/search/term.html?KEYWORDS=terrorist"
        self.starturl = "http://cn.rfi.fr/search/?Search%5Bterm%5D=%E6%81%90%E6%80%96&Search%5Bpage%5D=1"#法国

    def get_page_count(self,url,headers):
        '''
        获取新华网中，该关键词的总页面信息
        '''
        print "起始url是："+url
        html =None

        html=self.getUrl_multiTry(url,headers)
        # 对获取到的文本进行解析
        soup = BeautifulSoup(html,'lxml')
        # 从解析文件中通过select选择器定位指定的元素，返回一个列表
        result_count = soup.select("ul.list > p.search-summary-results")
        result_count = result_count[0].encode('gbk')
        result_count = filter(str.isdigit, result_count)
        print 'result_count--------',result_count
        
        page_count = soup.select("ol.pagination-search")
        page_count = str(page_count).split('%5D=')[-1]
        page_count = page_count.split('"')[0]
        #page_count = re.findall(r"\d+\.?\d*",str(page_count))
        print 'page_count--------',page_count
        pacgeCount = int(page_count)
        resultCount = int(result_count)

        return pacgeCount,resultCount
        
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
        
         # 对获取到的文本进行解析
        soup = BeautifulSoup(html,'html.parser')
        
#        # 从解析文件中通过select选择器定位指定的元素，返回一个列表
#        content_dict = soup.select("ul.list > li")
#        print len(content_dict)
#        print '---------------',100     
#        # 对返回的列表进行遍历
#        for n in content_dict:
#            # 提取出标题和链接信息
#            title = n.get_text()
#            #title = n.get("title")
#            time = n.get("datetime")
#            print 'n-------------',n
#            print '----------title',time,title
#            link = n.get("href")
#            print '----------link',link
#            data = {
#                '标题':title,
#                '链接':link
#            }
#            print(data)
        
        
        
        items = soup.select("ul.list")[0].find_all('li')#li,h3
        #times = soup.select("ul.list")[0].find_all('time')#li,h3
        url = soup.select("ul.list")[0].find_all('h3')#li,h3
        #img = soup.select("ul.list")[0].find_all('img')#li,h3
        
#        print '新闻',len(items),len(times),len(url),len(img)
#        print '时间---------',times[0]
#        print 'url-----------',url[0]

        #content_dict = items
        for i in range(len(items)):
            time = str(items[i].get_text()).split('\n')[5]
            titleStr = str(items[i].get_text()).split('\n')[-3]
            if titleStr  in self.titles:
                continue
            self.titles.append(titleStr)
            url_temp ='http://cn.rfi.fr' + str(url[i]).split('"')[5]
            index_result={}
#            print 'pubtime---------',time
#            print 'url-------------',url_temp
#            print 'title-----------',titleStr
            index_result["pubtime"] = time
            index_result["title"]=titleStr
            index_result["imgUrl"]=''
            index_result["url"]=url_temp
            index_result["content"]=""
            index_result["des"]=""
            index_result["keyword"] = 'img'
            result.append(index_result)
        return result
    def get_html_soup_txt(self,url,headers):#获取解编码后的HTML
        html = None


        html=self.getUrl_multiTry(url,headers)
        #fout = codecs.open("out3.txt",'w','utf-8')
        #fout.write(html)
        #fout.close()
        soup=BeautifulSoup(html, 'html.parser', from_encoding='utf-8') 
        return soup
    
    #get_html_soup_txt(urlTxt,my_headers)
    def get_html_soup(self,url,headers):#获取解编码后的HTML
        '''
        获取页面编码后的内容
        '''

        #try:
        #print "we are the url afsdfsdfsdfsdfsdfsdf",url

       
        if not url.startswith("http://"):
            url = "http://"+url
        #print url
        html = None
        html =self.getUrl_multiTry(url,headers)

        # html=urllib2.urlopen(req).read().decode(encoding = "utf8", errors='ignore')
        # fout = codecs.open("outtest%d.txt" % self.index,'w','utf-8')
        # fout.write(html)
        # fout.close()
        self.index+=1
        soup=BeautifulSoup(html, 'html.parser', from_encoding='utf-8') 
        #soup = BeautifulSoup(str(html), "lxml")
        return soup
    
    def page_url(self,url, page_num):#生成带页面的URL
        '''
        获取页面的url
        '''
        if page_num == 1:
            return url
        index = url.rfind(".")
        #print "{{{{{{{{{{{{{{{}}}}}}}}}}}}}}",url[0 : index] + "_" + str(page_num) + url[index : ]
        return url[0 : index] + "_" + str(page_num) + url[index : ]
    
    def get_title_link(self,url, pattern):#获取新闻的标题和正文链接
        #这里的pattern指的是获取的模式。
        soup = self.get_html_soup(url,self.my_headers)
        news_link = {}
    
        scroll_list = BeautifulSoup(str(soup.find("div", attrs = pattern)), "lxml")
        for link in scroll_list.find_all("a"):
            if len(link.get_text().strip()) > 0 and link.get("href").find("http") != -1:
                news_link[link.get_text()] = link.get('href')
        return news_link
    
    def get_news_body(self,url,headers):#抓取新闻主体内容
        '''
        获取新闻的主要内容
        '''
        result={}
        #使用循环处理有分页的新闻
        soup = self.get_html_soup(url,self.my_headers)
        if soup == None:
            return None
        texts = soup.find_all('p')
        content_text = ""
        for index in range(len(texts)):
            text=texts[index]
            content_text += text.get_text()
        result["content"]=content_text.split('\n')[0]
#        try:
#            result["time"]=soup.find('div',class_="sj").get_text()
#            print 'time----',result["time"]
#        except:
#            result["time"]=""
#        try:
#            result["source"]=soup.find('div',class_="ly").get_text()
#            print 'source----',result["source"]
#        except:
#            result["source"]=""
        try:
            temp_url = soup.find('div',class_="media")
            result["imgUrl"] = str(temp_url).split('src="')[1].split('"')[0]
            print 'imgurl-----------',result["imgUrl"]
        except:
            result["img"]=""
        try:
            temp_name = soup.find('div',class_="media")
            result["imgName"] = str(temp_name).split('small>')[1].replace('</','')
            print 'imgname-------------',result["imgName"]
        except:
            result["imgName"]=""
        return result
    
    def clean_chinese_character(self,text):
        '''处理特殊的中文符号,将其全部替换为'-' 否则在保存时Windows无法将有的中文符号作为路径'''
        chars = chars = ["/", "\"", "'", "·", "。","？", "！", "，", "、", "；", "：", "‘", "’", "“", "”", "（", "）", "…", "–", "．", "《", "》"];
        new_text = ""
        for i in range(len(text)):
            if text[i] not in chars:
                new_text += text[i]
            else:
                new_text += "_"
        return new_text;
    def createFile(self,fields,zhFileName):
        # 新建一个excel文件  
        zhFile = xlwt.Workbook(encoding='utf-8')  
        # 新建一个sheet  
        zhTable = zhFile.add_sheet('Data', cell_overwrite_ok=True)  
        for index in range(len(fields)):
            zhTable.write(0, index, fields[index])
        zhFile.save(zhFileName)
        return zhFile,zhTable
        
    def saveData(fields,eventInfo,zhFile,zhTable,rowNum,zhFileName):
        
        for index in range(len(fields)):
            zhTable.write(rowNum,index,eventInfo[fields[index]])
        #if(rowNum%50==0):
        #    zhFile.save(zhFileName+".xls");
    def get_Hash(self,data):
        '''
        计算Hash值
        '''
        data = data.encode('utf-8')
        #print data
        m = md5()
        m.update(data)
        urlHash = m.hexdigest()
        #print urlHash
        return urlHash
    def start_crawl(self):
        '''
        这个函数开始爬取数据
        '''
        #获取到页面和条目统计信息
        fileName=''
        stopFlag = False
        CrawlData={}
        #FilterData={}
        pages,indexcount = self.get_page_count(self.starturl,self.my_headers)
        fields = ["reporttime","reporter","title","sitename","keyword","content","imgUrl"]
        #根据是否需要记录文件来进行
        EventInfoExtract = fact_triple_extraction1chen.EventInfoExtract(r"3.3.0\ltp_data",'out123.txt')
        index = 0
        #遍历所有的新闻页
        for i in range(1,pages+1):
            #得到当前页的url
            urls =self.starturl.replace("curPage=1","curPage=%d" % i)
            #返回数组对象，每个元素表示一条新闻的简略信息
            infodexs = self.index_info(urls,self.my_headers)
            if len(infodexs)>0:
                for infodex in infodexs:
                    #判断是否达到终止天数
                    if self.deadlineTime!=0 and infodex["reporttime"][0:10]<self.deadlineTime: #终止爬取
                        stopFlag=True
                        if(EventInfoExtract.segmentor != None): 
                            EventInfoExtract.release_module()
                        break
                    if(infodex["keyword"]=="视频"):
                        continue
                    print "=====================新闻信息=========================="
                    print infodex["url"]
                    body = self.get_news_body(infodex["url"],self.my_headers)
                    if body!=None:
                        infodex["content"]=body["content"]
                        infodex["reporter"]=u"法国电视广播电视台"
                        infodex["imgUrl"]=body["imgUrl"]
                        infodex["imgName"]=body["imgName"]
                    index+=1
                    #恢复为原来的段落
                    datas = infodex["content"].split(u"　　")
                    EventInfoExtract.InitModule()
                
                    #print '数据-----------------', datas
                    for data in datas:
                        print data.encode("utf-8")

                        if len(data.encode("utf-8"))<30 or data.encode("utf-8")==None:
                            continue
                        TimeAndAddress=EventInfoExtract.addresssTime_extract(data.encode("utf-8"))
                        #print TimeAndAddress
                        fact_attribute = EventInfoExtract.fact_attribute_from_text(data.encode("utf-8"))
                        orgnization = EventInfoExtract.organization_from_text(data.encode("utf-8"))
                        death_num,hurt_num,total_num = EventInfoExtract.death_num_from_text(data.encode("utf-8"))
                        if TimeAndAddress[0]["date"]=="" and TimeAndAddress[0]["address"]=="":
                            continue
                        print '''  
    时间\t地点\t事件类型\t攻击组织\t伤亡总人数\t死亡人数\t受伤人数
    %s--%s--%s--%s--%s--%s--%s'''%(TimeAndAddress[0]['date'],TimeAndAddress[0]['address'],fact_attribute,orgnization,total_num,death_num,hurt_num)
                    # print("start to releases")

                    #将新闻的原文也进行保存

                    imgUrl=infodex["imgUrl"]
                    imgName=infodex["imgName"]
                    if(imgUrl!=None and imgUrl!=""):
                        imgName=imgUrl.split("/")[-1]
                        urlretrieve("http://tpic.home.news.cn/xhCloudNewsPic/"+imgUrl,"./imgs/"+ imgName)
                    print infodex
                    news={}
                    news["title"]=infodex["title"]
                    news["des"]=infodex["des"]
                    news["pubtime"] =infodex["pubtime"]
                    news["content"]=infodex["content"]
                    news["img"]=imgName
                    news["url"]=infodex["url"]

                    news['time']=TimeAndAddress[0]['date']
                    news['address']=TimeAndAddress[0]['address']
                    news['type']=fact_attribute

                    if(total_num!=None):
                        news['total']="伤亡:" + total_num
                    else:
                        if death_num==None:
                            death_num="0"
                        if hurt_num==None:
                            hurt_num="0"
                        # print death_num, hurt_num
                        news['total']="死亡：" + death_num + "，受伤：" + hurt_num
                    news["gname"]=orgnization
                    news['nwound']=hurt_num
                    news['nkill']=death_num

                    # insertSql = db_connect.generateSQL(news)
                    # print insertSql
                    # db_connect.insertOneData(insertSql)


                    # PostData(data,hosturl)
                    EventInfoExtract.release_module()

                if stopFlag ==True:
                    print "sTOPP ING"
                    break
        if(EventInfoExtract.segmentor != None):
            EventInfoExtract.release_module()
        sys.exit(0)
        print "Here Release-=======--==="

    def get_content(self,html):
        # 内容分割的标签
        soup = BeautifulSoup(html,'lxml')
        #content = soup.select("ul.list > h3. ")
        content = soup.select("h3.  > a.modeless ")
        print '-----------内容',content[0]['title']
        print len(content)

        return content # 得到搜索列表的新闻标题和链接
    
    def getUrl_multiTry(self,url,headers):
        time.sleep(1)
        maxTryNum = 10
        for tries in range(maxTryNum):
            try:
                randddom_header = random.choice(headers)
                req = urllib2.Request(url)
                req.add_header("User-Agent", randddom_header)
                req.add_header("GET", url)
                
                proxy_info = { 'host' : 'imagesoft.dynu.com',
                              'port' : 8000}   #设置你想要使用的代理  
                proxy_support = urllib2.ProxyHandler({"http" : "http://%(host)s:%(port)d" % proxy_info})       
                opener = urllib2.build_opener(proxy_support)        
                urllib2.install_opener(opener)
                
                html = urllib2.urlopen(req).read().decode(encoding="utf8", errors='ignore')
                #html = urllib2.urlopen(req).read()
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
    xinhuaCrawl = Crawl_Xinhua(timeFrame=0,saveFile=True)
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
    
    
    