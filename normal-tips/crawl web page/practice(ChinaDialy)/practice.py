# -*- coding: utf-8 -*-

"""
后期可以修改的！

1、针对网站的域名进行爬取，中国日报网的域名上的所有网页应该都是相同格式的。可以用正则表达式
    eg: http://world.chinadaily.com.cn/2017-04/05/content_28798021.htm
    http://world.chinadaily.com.cn/   对应的格式
    eg: http://cnews.chinadaily.com.cn/2017-04/04/content_28791640.htm
    http://cnews.chinadaily.com.cn/   对应的格式

2、注意，try可以用在调试，但是要记得打印出错误，同时兼顾单步调试，像爬虫这样的代码，用try except 来
注意爬取网站不行就continue是很好的做法。

3、to_join = [content_p[k].text for k in range(len(content_p))] 语句简单明了，通俗好用

4、本代码加入了pyltp进行相关的段落短语提取，但是出现了不同的错误，基本指向segment fault，
    目前原因尚未查明。

5、曾经遇见过一个问题，在爬取网页的时候遇见了动态页面，翻页时页面链接是一样的，猜测用到了Ajax。
    有软件可以解决这个问题。(Phantomjs软件)，一个基于webkit内核的无头浏览器，即没有UI界面，
    即它就是一个浏览器，只是其内的点击、翻页等人为相关操作需要程序设计实现。

"""

from baike_spider import url_manager, html_downloader, html_parser, html_outputer
import fact_triple_extraction1chen


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        for i in range(149):
            start_url = root_url.replace("page=1", "page=%d" % count)
            html = self.downloader.download(start_url)
            # print html
            new_urls = self.parser.parse(start_url, html)
            self.urls.add_new_urls(new_urls)
            print 'craw %d %s' % (count, start_url)
            count = count + 1

        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('id %d' % count)
                html_cont = self.downloader.download(new_url)
                self.content = []
                title, time, des, content, img_url = self.parser.get_data(new_url, html_cont)
                print(title, time, des, self.content)
                print('==========================================')
            except Exception as e:
                print(e)
                continue


            EventInfoExtract = fact_triple_extraction1chen.EventInfoExtract(r"3.3.0\ltp_data", 'out123.txt')
            EventInfoExtract.InitModule()

            TimeAndAddress = EventInfoExtract.addresssTime_extract(content.encode("utf-8"))
            # print TimeAndAddress
            fact_attribute = EventInfoExtract.fact_attribute_from_text(content.encode("utf-8"))
            orgnization = EventInfoExtract.organization_from_text(content.encode("utf-8"))
            death_num, hurt_num, total_num = EventInfoExtract.death_num_from_text(content.encode("utf-8"))
            # if TimeAndAddress[0]["date"] == "" and TimeAndAddress[0]["address"] == "":
            #     continue
            print '''  time\t address\t type\t orgnize\t total\t dead\t hurt%s--%s--%s--%s--%s--%s--%s''' % (
            TimeAndAddress[0]['date'], TimeAndAddress[0]['address'], fact_attribute, orgnization, total_num, death_num, hurt_num)

            # basis datas
            news = {}
            news['id'] = count
            news['pubtime'] = time
            news['title'] = title
            news['des'] = des
            news['content'] = content
            news['url'] = new_url
            news['img'] = img_url

            # exact datas
            news['time'] = TimeAndAddress[0]['date']
            news['address'] = TimeAndAddress[0]['address']
            news['type'] = fact_attribute
            if (total_num != None):
                news['total'] = "total:" + total_num
            else:
                if death_num == None:
                    death_num = "0"
                if hurt_num == None:
                    hurt_num = "0"
                # print death_num, hurt_num
                news['total'] = "dead:" + death_num + ", hurt:" + hurt_num
            news['gname'] = orgnization
            news['nwound'] = hurt_num
            news['nkill'] = death_num

            datas = []
            datas.append(news)
            self.outputer.output_execl(datas, "ChinaDialy.csv", count)
            count = count + 1
            EventInfoExtract.release_module()

        # self.urls.add_new_url(root_url) # crawl all page
        # while self.urls.has_new_url():
        #     try:
        #         new_url = self.urls.get_new_url()
        #         print 'craw %d: %s' % (count, new_url)
        #         html_cont = self.downloader.download(new_url)
        #         # print html_cont
        #         new_urls, new_data = self.parser.parse(new_url, html_cont)
        #         self.urls.add_new_url(new_urls)
        #         self.outputer.collect_data(new_data)
        #         count = count + 1
        #         if count >= 100:
        #             break
        #     except Exception as e:
        #         print(e)
        #         print 'craw failed'

        # self.outputer.output_html()


if __name__=="__main__":
    root_url = "http://search.chinadaily.com.cn/cn.jsp?searchText=%E6%81%90%E6%80%96%E8%A2%AD%E5%87%BB&page=1&strAuthor=&strFromdate=&strTodate=&usedate="
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
