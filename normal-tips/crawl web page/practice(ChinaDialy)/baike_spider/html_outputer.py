import os
import csv

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()


    def output_execl(self, data, file, page):
        import codecs
        import sys
        # reload(sys) 版本问题引起的暂时注释日后修改
        sys.setdefaultencoding('utf8')

        headers = [u'id', u'pubtime', u'title', u'des', u'content', u'img', u'url', u'time',
                   u'address', u'type', u'gname', u'nwound', u'nkill', u'total']
        headerflag = True
        if os.path.exists(file):
            headerflag = False
        with codecs.open(file, 'ab+', 'utf8') as f:
            f_csv = csv.DictWriter(f, headers)
            if headerflag:
                f_csv.writeheader()
            f_csv.writerows(data)
        print('page %d save to \'%s\' sucessfully!' % (page, file))