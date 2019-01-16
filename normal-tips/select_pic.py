import wx

class ImageWindow(wx.Window):

    def __init__(self, parent, id):
        wx.Window.__init__(self, parent, id)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.image = None

    def SetImage(self, image):
        self.image = image
        self.Refresh(True)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        if self.image:
            dc.DrawBitmap(self.image.ConvertToBitmap(), 0, 0, False)


class AppFrame(wx.Frame):

    def __init__(self, parent, ID, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)

        vbox = wx.BoxSizer(wx.VERTICAL)
        topBox = wx.BoxSizer(wx.HORIZONTAL)
        botBox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(topBox, 1, wx.EXPAND)
        vbox.Add(botBox)

        btnA = wx.Button(self, wx.ID_ANY, 'Button A')
        # self.Bind(wx.EVT_BUTTON, self.OnClick, self.btnA)
        btnB = wx.Button(self, wx.ID_ANY, 'Button B')

        botBox.Add(btnA)
        botBox.Add(btnB)

        imw = ImageWindow(self, wx.ID_ANY)
        topBox.Add(imw, 1, wx.EXPAND)

        image = wx.Image('LFPW_image_test_0071_2_LFPW_image_train_0294_0.jpg', wx.BITMAP_TYPE_JPEG)
        imw.SetImage(image)

        self.SetSizer(vbox)

    # def OnClick(self,evt):
    # image = wx.Image('bbb.png', wx.BITMAP_TYPE_PNG)


    # imw.SetImage(image)


class MyApplication(wx.App):

    def OnInit(self):
        wnd = AppFrame(None, wx.ID_ANY, "Main Window")
        wnd.Show(True)
        return True


def main():
    app = MyApplication(False)
    app.MainLoop()


if __name__ == "__main__":
    main()