"""
需要改的是main里面的frame = CleanerFrame(中文文档路径, 英文文档路径, 起始的事件id)
需要注意的是把文档另存为csv格式再输入

"""
from ulits import Data
import wx
import csv
import argparse
import codecs
ROW = 30
EN_COL = 20
CN_COL = 500

TXT_ID = ['country_txt','provstate','city','summary','targtype1_txt',
          'corp1','target1','gname','motive','weapdetail',
          'propcomment','ransomnote','hostkidoutcome_txt','addnotes','scite1']

def write_csv(path, list_stream):
    csvFile = codecs.open(path, "w", 'utf-8')
    for stream in list_stream:
        try:
            content = ','.join(stream) + '\n'
            csvFile.write(content)
        except Exception as e:
            a=1
    # writer = csv.writer(csvFile)
    # for stream in list_stream:
    #     writer.writerow(stream)
    csvFile.close()


def read_csv(path):
    list_num = []
    dict_id = {}
    dict_mesg = {}
    reader = []
    csv_reader = csv.reader(open(path, encoding='utf-8'))
    for row in csv_reader:
        reader.append(row)
    list_id = reader[0]
    del reader[0]
    for mesg in  reader:
        list_num.append(mesg[0].strip())
        for i in range(len(list_id)-1):
            dict_mesg[list_id[i + 1]] = mesg[i + 1]
        dict_id[mesg[0].strip()] = dict_mesg
        dict_mesg = {}

    return list_num, dict_id

class readDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'data input', size=(300, 100))
        panel = wx.Panel(self, -1)

        sizer = wx.BoxSizer(wx.VERTICAL)
        cnStaticText = wx.StaticText(panel, -1, '中文表路径:')
        self.cnText = wx.TextCtrl(panel, value='', size=(230, 30))
        enStaticText = wx.StaticText(panel, -1, '英文表路径')
        self.enText = wx.TextCtrl(panel, value='', size=(230, 30))
        IDStaticText = wx.StaticText(panel, -1, '事件ID')
        self.idText = wx.TextCtrl(panel, value='', size=(230, 30))
        openButton = wx.Button(panel, label='OK', pos=(120, 100), size=(110, 30))
        sizer.Add(cnStaticText, 0)
        sizer.Add(self.cnText, 0)
        sizer.Add(enStaticText, 0)
        sizer.Add(self.enText, 0)
        sizer.Add(IDStaticText, 0)
        sizer.Add(self.idText, 0)
        sizer.Add(openButton, 0)

        panel.SetSizer(sizer)
        sizer.SetSizeHints(self)
        panel.Layout()
        panel.SetFocus()

        openButton.Bind(wx.EVT_BUTTON, self.onClickOpen)

    def onClickOpen(self, event):
        cn_path = self.cnText.GetValue()
        en_path = self.enText.GetValue()
        id_n = self.idText.GetValue()
        app = wx.App()
        frame = CleanerFrame(cn_path, en_path, id_n)
        frame.Show()
        app.MainLoop()


class CleanerFrame(wx.Frame):
    def __init__(self, cn_path, en_path, id):
        wx.Frame.__init__(self, None, -1, "data clean",
                          size=(1000, 800))

        self.list_cn, self.dict_cn = read_csv(cn_path)
        self.list_en, self.dict_en = read_csv(en_path)
        self.row = self.list_cn.index(str(id))
        self.count = 0
        event_str_cn = self.dict_cn[str(id)]
        event_str_en = self.dict_en[str(id)]
        tx_en = []
        tx_cn = []
        for i in range(5):
            tx_en.append(event_str_en[TXT_ID[self.row * 5 + i]])
            tx_cn.append(event_str_cn[TXT_ID[self.row * 5 + i]])
        # init_en = init_en[id_cn[self.col + 1]]
        # while not init_en.__contains__(self.id_cn[self.col + 1]):
        #     self.col += 1
        # init_en = init_en[self.id_cn[self.col + 1]]
        # init_cn = self.dict_cn[self.list_cn[self.row]]
        # init_cn = init_cn[self.id_cn[self.col + 1]]
        str_id = 'eventid = ' + self.list_cn[self.row]


        panel = wx.Panel(self, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        upButton = wx.Button(panel, -1, '上一条', pos=(20, 500))
        downButton = wx.Button(panel, -1, '下一条', pos=(150, 500))
        downButton.SetDefault()
        saveButton = wx.Button(panel, -1, '保存', pos=(250, 500))
        self.staticText_id = wx.StaticText(panel, -1, label=str_id, pos=(0, 10))

        staticText_en = wx.StaticText(panel, -1, label='EN', pos = (EN_COL, ROW))
        self.en1 = wx.TextCtrl(panel, value=tx_en[0], pos=(EN_COL, ROW + 20), size=(400, 60), style = wx.TE_MULTILINE|wx.HSCROLL)
        self.en2 = wx.TextCtrl(panel, value=tx_en[1], pos=(EN_COL, ROW + 90), size=(400, 60), style=wx.TE_MULTILINE | wx.HSCROLL)
        self.en3 = wx.TextCtrl(panel, value=tx_en[2], pos=(EN_COL, ROW + 160), size=(400, 60), style=wx.TE_MULTILINE | wx.HSCROLL)
        self.en4 = wx.TextCtrl(panel, value=tx_en[3], pos=(EN_COL, ROW + 230), size=(400, 60), style=wx.TE_MULTILINE | wx.HSCROLL)
        self.en5 = wx.TextCtrl(panel, value=tx_en[4], pos=(EN_COL, ROW + 300), size=(400, 60), style=wx.TE_MULTILINE | wx.HSCROLL)

        staticText_cn = wx.StaticText(panel, -1, label='CN', pos=(CN_COL, ROW))
        self.cn1 = wx.TextCtrl(panel, value=tx_cn[0], pos=(CN_COL, ROW + 20), size=(400, 60),style=wx.TE_MULTILINE | wx.HSCROLL)
        self.cn2 = wx.TextCtrl(panel, value=tx_cn[1], pos=(CN_COL, ROW + 90), size=(400, 60),style=wx.TE_MULTILINE | wx.HSCROLL)
        self.cn3 = wx.TextCtrl(panel, value=tx_cn[2], pos=(CN_COL, ROW + 160), size=(400, 60),style=wx.TE_MULTILINE | wx.HSCROLL)
        self.cn4 = wx.TextCtrl(panel, value=tx_cn[3], pos=(CN_COL, ROW + 230), size=(400, 60),style=wx.TE_MULTILINE | wx.HSCROLL)
        self.cn5 = wx.TextCtrl(panel, value=tx_cn[4], pos=(CN_COL, ROW + 300), size=(400, 60),style=wx.TE_MULTILINE | wx.HSCROLL)

        self.staticReform = wx.StaticText(panel, -1, label='', pos=(20, 300))

        sizer.Add(self.staticText_id, 0)
        sizer.Add(staticText_en, 0)
        sizer.Add(self.en1, 0)
        sizer.Add(self.en2, 0)
        sizer.Add(self.en3, 0)
        sizer.Add(self.en4, 0)
        sizer.Add(self.en5, 0)
        sizer.Add(staticText_cn, 0)
        sizer.Add(self.cn1, 0)
        sizer.Add(self.cn2, 0)
        sizer.Add(self.cn3, 0)
        sizer.Add(self.cn4, 0)
        sizer.Add(self.cn5, 0)

        sizer.Add(self.staticReform, 0)

        upButton.Bind(wx.EVT_BUTTON, self.onClickUp)
        downButton.Bind(wx.EVT_BUTTON, self.onClickDown)
        saveButton.Bind(wx.EVT_BUTTON, self.onClickSave)

    def onClickUp(self, event):
        self.staticReform.SetLabel('')
        value = self.cnText.GetValue()
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn[self.id_cn[self.col + 1]] = value
        self.col -= 1
        if self.col < 0:
            self.col = len(self.id_cn) - 2
            self.row -= 1
            if self.row < 0:
                self.row = len(self.list_cn) - 1
        key = self.list_cn[self.row]
        init_en = self.dict_en[key]
        # init_en = init_en[id_cn[self.col + 1]]
        while not init_en.__contains__(self.id_cn[self.col + 1]):
            self.col -= 1
            if self.col < 0:
                self.col = len(self.id_cn) - 2
                self.row -= 1
                if self.row < 0:
                    self.row = len(self.list_cn) - 1
        init_en = init_en[self.id_cn[self.col + 1]]
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn = init_cn[self.id_cn[self.col + 1]]
        while init_cn == '':
            self.col -= 1
            if self.col < 0:
                self.col = len(self.id_cn) - 2
                self.row -= 1
                if self.row < 0:
                    self.row = len(self.list_cn) - 1
            key = self.list_cn[self.row]
            init_en = self.dict_en[key]
            # init_en = init_en[id_cn[self.col + 1]]
            while not init_en.__contains__(self.id_cn[self.col + 1]):
                self.col -= 1
                if self.col < 0:
                    self.col = len(self.id_cn) - 2
                    self.row -= 1
                    if self.row < 0:
                        self.row = len(self.list_cn) - 1
            init_en = init_en[self.id_cn[self.col + 1]]
            init_cn = self.dict_cn[self.list_cn[self.row]]
            init_cn = init_cn[self.id_cn[self.col + 1]]

        str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
        self.staticText_id.SetLabel(str_id)
        self.enText.SetValue(init_en)
        self.cnText.SetValue(init_cn)


    def onClickDown(self, event):
        self.staticReform.SetLabel('')
        value = self.cnText.GetValue()
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn[self.id_cn[self.col + 1]] = value
        self.col += 1
        if self.col >= (len(self.id_cn)-1):
            self.col = 0
            self.row += 1
            if self.row >= len(self.list_cn):
                self.row = 0
        key = self.list_cn[self.row]
        init_en = self.dict_en[key]
        # init_en = init_en[id_cn[self.col + 1]]
        while not init_en.__contains__(self.id_cn[self.col + 1]):
            self.col += 1
        init_en = init_en[self.id_cn[self.col + 1]]
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn = init_cn[self.id_cn[self.col + 1]]
        while init_cn == '':
            self.col += 1
            if self.col >= (len(self.id_cn) - 1):
                self.col = 0
                self.row += 1
                if self.row >= len(self.list_cn):
                    self.row = 0

            key = self.list_cn[self.row]
            init_en = self.dict_en[key]
            while not init_en.__contains__(self.id_cn[self.col + 1]):
                self.col += 1
            init_en = init_en[self.id_cn[self.col + 1]]
            init_cn = self.dict_cn[self.list_cn[self.row]]
            init_cn = init_cn[self.id_cn[self.col + 1]]

        str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
        self.staticText_id.SetLabel(str_id)
        self.enText.SetValue(init_en)
        self.cnText.SetValue(init_cn)

    def onClickSave(self, event):
        list_csv = []
        list_csv.append(self.id_cn)
        for i in range(len(self.list_cn)):
            list_line = []
            list_line.append(self.list_cn[i])
            for j in range(len(self.id_cn) - 1):
                cn = self.dict_cn[self.list_cn[i]]
                list_line.append(cn[self.id_cn[j + 1]])
            list_csv.append(list_line)

        write_csv('new.csv', list_stream=list_csv)
        self.staticReform.SetLabel('保存成功')


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='data cleaner')
    # group = parser.add_mutually_exclusive_group()
    # parser.add_argument('-c', '--cnpath', help='CN path', type=str)
    # parser.add_argument('-e', '--enpath', help='EN path', type=str)
    # parser.add_argument('-i', '--id', help='ID', type=str)
    # args = parser.parse_args()

    app = wx.App()
    dialog = readDialog()
    result = dialog.ShowModal()
    if result == wx.ID_CANCEL:
        print('cancel')
    else:
        pass
    dialog.Destroy()

# python3 data_cleaner.py -c 'Chinese.csv' -e 'English.csv', -i 197000000002