"""


"""
import wx
import csv

class CleanerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "data clean",
                          size=(1000, 800))
        dict_id = {}
        dict_mesg = {}
        csv_reader = csv.reader(open('Chinese.csv', encoding='utf-8')) #list
        
        for row in  csv_reader:
            mesg = row.split(';')
            dict_mesg[]
            dict_id[mesg[0]] = dict_mesg






        panel = wx.Panel(self, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(20, 120))
        okButton.SetDefault()
        cancelButton = wx.Button(self, wx.ID_CANCEL, 'Cancel', pos=(150, 120))
        staticText_id = wx.StaticText(self, -1, label='eventid=199301000001，id=eventid', pos=(0, 10))
        staticText_en = wx.StaticText(self, -1, label='EN', pos = (20, 10))
        self.enText = wx.TextCtrl(self, value='', pos=(20, 30), size=(160, 30))
        staticText_ch = wx.StaticText(self, -1, label='CH', pos=(20, 60))
        self.chText = wx.TextCtrl(self, value='', pos=(20, 80), size=(160, 30))


        sizer.Add(staticText_id, 0)
        sizer.Add(staticText_en, 0)
        sizer.Add(self.enText, 0)
        sizer.Add(staticText_ch, 0)
        sizer.Add(self.chText, 0)



if __name__ == '__main__':
    app = wx.App()
    frame = CleanerFrame()
    frame.Show()
    app.MainLoop()
