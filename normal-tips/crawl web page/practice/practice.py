
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
        for i in range(2):#21
            start_url = root_url.replace("offset=20", "offset=%d" % count)
            html = self.downloader.download(start_url)
            # print html
            new_urls = self.parser.parse(start_url, html)
            self.urls.add_new_urls(new_urls)
            print 'craw %d %s' % (count, start_url)
            count = count + 20

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
            self.outputer.output_execl(datas, "SputnikNews.csv", count)
            count = count + 1

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
    root_url = "http://sputniknews.cn/services/search/getmore/?search_area=all&query%5B%5D=%E6%81%90%E6%80%96%E8%A2%AD%E5%87%BB&limit=500&offset=20&sort=date&interval=period"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
