"""


"""
# from ulits import Data
import wx
import csv

def write_csv(path, list):
    csvFile = open(path, "w")
    writer = csv.writer(csvFile)
    writer.writerow(list)
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

    return list_id, list_num, dict_id


class CleanerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "data clean",
                          size=(1000, 800))
        self.row = 0
        self.col = 0
        self.id_cn, self.list_cn, self.dict_cn = read_csv('Chinese.csv')
        self.id_en, self.list_en, self.dict_en = read_csv('English.csv')
        str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
        key = self.list_cn[self.row]
        init_en = self.dict_en[key]
        # init_en = init_en[id_cn[self.col + 1]]
        while not init_en.__contains__(self.id_cn[self.col + 1]):
            self.col += 1
        init_en = init_en[self.id_cn[self.col + 1]]
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn = init_cn[self.id_cn[self.col + 1]]
        panel = wx.Panel(self, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        upButton = wx.Button(panel, -1, '上一条', pos=(20, 160))
        downButton = wx.Button(panel, -1, '下一条', pos=(150, 160))
        downButton.SetDefault()
        saveButton = wx.Button(panel, -1, '保存', pos=(250, 160))
        self.staticText_id = wx.StaticText(panel, -1, label=str_id, pos=(0, 10))
        staticText_en = wx.StaticText(panel, -1, label='EN', pos = (20, 30))
        self.enText = wx.TextCtrl(panel, value=init_en, pos=(20, 50), size=(160, 30))
        staticText_cn = wx.StaticText(panel, -1, label='CN', pos=(20, 90))
        self.cnText = wx.TextCtrl(panel, value=init_cn, pos=(20, 110), size=(160, 30))

        sizer.Add(self.staticText_id, 0)
        sizer.Add(staticText_en, 0)
        sizer.Add(self.enText, 0)
        sizer.Add(staticText_cn, 0)
        sizer.Add(self.cnText, 0)

        upButton.Bind(wx.EVT_BUTTON, self.onClickUp)
        downButton.Bind(wx.EVT_BUTTON, self.onClickDown)
        saveButton.Bind(wx.EVT_BUTTON, self.onClickSave)

    def onClickUp(self, event):
        value = self.cnText.GetValue()
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn[self.id_cn[self.col + 1]] = value
        self.col -= 1
        if self.col < 0:
            self.col = len(self.id_cn) - 1
            self.row -= 1
        str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
        self.staticText_id.SetLabel(str_id)
        key = self.list_cn[self.row]
        init_en = self.dict_en[key]
        # init_en = init_en[id_cn[self.col + 1]]
        while not init_en.__contains__(self.id_cn[self.col + 1]):
            self.col += 1
        init_en = init_en[self.id_cn[self.col + 1]]
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn = init_cn[self.id_cn[self.col + 1]]
        while init_cn == '':
            self.col -= 1
            if self.col < 0:
                self.col = len(self.id_cn) - 1
                self.row -= 1
            str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
            self.staticText_id.SetLabel(str_id)
            key = self.list_cn[self.row]
            init_en = self.dict_en[key]
            # init_en = init_en[id_cn[self.col + 1]]
            while not init_en.__contains__(self.id_cn[self.col + 1]):
                self.col += 1
            init_en = init_en[self.id_cn[self.col + 1]]
            init_cn = self.dict_cn[self.list_cn[self.row]]
            init_cn = init_cn[self.id_cn[self.col + 1]]

        self.enText.SetValue(init_en)
        self.cnText.SetValue(init_cn)


    def onClickDown(self, event):
        value = self.cnText.GetValue()
        init_cn = self.dict_cn[self.list_cn[self.row]]
        init_cn[self.id_cn[self.col + 1]] = value
        self.col += 1
        if self.col >= (len(self.id_cn)-1):
            self.col = 0
            self.row += 1
        str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
        self.staticText_id.SetLabel(str_id)
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
            str_id = 'eventid = ' + self.list_cn[self.row] + '，id = ' + self.id_cn[self.col + 1]
            self.staticText_id.SetLabel(str_id)
            key = self.list_cn[self.row]
            init_en = self.dict_en[key]
            # init_en = init_en[id_cn[self.col + 1]]
            while not init_en.__contains__(self.id_cn[self.col + 1]):
                self.col += 1
            init_en = init_en[self.id_cn[self.col + 1]]
            init_cn = self.dict_cn[self.list_cn[self.row]]
            init_cn = init_cn[self.id_cn[self.col + 1]]

        self.enText.SetValue(init_en)
        self.cnText.SetValue(init_cn)

    def onClickSave(self, event):
        pass







if __name__ == '__main__':
    app = wx.App()
    frame = CleanerFrame()
    frame.Show()
    app.MainLoop()
