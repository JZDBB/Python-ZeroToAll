
from bs4 import BeautifulSoup
import unicodedata
import urlparse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('h2') # href=re.compile(r"/view/\d+.htm"))
        for link in links:
            url_ = link.find('a')
            new_url = url_['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    # def _get_new_urls(self, page_url, soup):
    #     new_urls = set()
    #     links = soup.find_all('a')
    #     for link in links:
    #         try:
    #             new_url = link['href']
    #         except:
    #             continue
    #         new_full_url = urlparse.urljoin(page_url, new_url)
    #         new_urls.add(new_full_url)
    #     return new_urls
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # print(html_cont)
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # new_urls = self._get_new_urls(page_url, soup)
        # new_data = self._get_new_data(page_url, soup)
        urls = self._get_new_urls(page_url, soup)
        return urls

    def get_data(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # print soup

        title_node = soup.find("h1")
        title = title_node.get_text()

        time_node = soup.find('time', class_="b-article__refs-date")
        # if time_node == None:
        #     time_ = soup.find('div', class_='arcform').find_all('span')
        #     time_node = time_[2]
        time_ = time_node['datetime']
        time_ = unicodedata.normalize('NFKD', time_).encode('ascii', 'ignore')
        time_ = time_.replace('T', ' ')
        time = unicode(time_)

        des_node = soup.find('div', class_="b-article__lead").find('p')
        des = des_node.get_text()

        content_node = soup.find('div', class_="b-article__text")
        content = content_node.get_text()
        content = u''.join(des)


        # content_p = content_node[0].select('p')
        # to_join = [content_p[k].text for k in range(len(content_p))]
        # content = u''.join(to_join)

        # img_node = soup.select("center")
        # if img_node:
        #     img = img_node[0].select('img')
        #     if img:
        #         img_url = img[0]['src']
        # else:
        #     img_url = u' '
        img = []

        img_node1 = soup.find('div', class_="b-article__header").find('img')
        img_node2 = soup.find('div', class_="b-inject__media").find('img')
        if img_node1 != None and img_node2 != None:
            img.append(img_node1['src'])
            img.append(img_node2['src'])
            img_url = u';'.join(img)
        elif img_node1 == None:
            img_url = img_node2['src']
        elif img_node2 ==None:
            img_url = img_node1['src']
        else:
            img_url = u''

        return title, time, des, content, img_url