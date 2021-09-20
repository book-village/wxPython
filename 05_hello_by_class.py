import wx


class Myframe(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('hello world')
        self.SetSize((500, 500))


class Myapp(wx.App):
    def OnInit(self):
        frame = Myframe(parent=None)
        frame.Show()
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    app = Myapp()
    app.MainLoop()
