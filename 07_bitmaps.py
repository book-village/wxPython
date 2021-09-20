import wx


class Myframe(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetTitle('hello world')
        self.CreateStatusBar()
        self.create_menu()
        bitmap1 = wx.Image('WxPython-logo.png').ConvertToBitmap()
        bitmap2 = wx.Image('WxPython-logo2.png').ConvertToBitmap()
        self.b1 = wx.StaticBitmap(parent=self, bitmap=bitmap1, size=bitmap1.GetSize())
        self.b2 = wx.StaticBitmap(parent=self, bitmap=bitmap2, size=bitmap2.GetSize())
        self.b2.Hide()
        self.SetClientSize(self.b1.GetSize())
        self.b1.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.b2.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.sw = 0

    def OnClick(self, event):
        self.sw = 1 - self.sw
        if self.sw == 1:
            self.b1.Hide()
            self.b2.Show()
        else:
            self.b1.Show()
            self.b2.Hide()

    def create_menu(self):
        # ファイルメニュー
        f_menu = wx.Menu()
        """第一パラメータには、メニューコマンドIDを指定します。-1は特には指定なしという意味"""
        f_menu.Append(-1, '新規', '新規作成')
        exit = f_menu.Append(-1, '終了', '終了します。')

        # 選択メニュー
        s_menu = wx.Menu()
        img1 = s_menu.Append(-1, '画像1', '画像1を選択します。')
        img2 = s_menu.Append(-1, '画像2', '画像2を選択します。')

        m_bar = wx.MenuBar()
        m_bar.Append(f_menu, 'ファイル')
        m_bar.Append(s_menu, '選択')
        self.SetMenuBar(m_bar)

        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        self.Bind(wx.EVT_MENU, self.OnSelectImg1, img1)
        self.Bind(wx.EVT_MENU, self.OnSelectImg2, img2)

    def OnExit(self, event):
        self.Close()


    def OnSelectImg1(self, event):
        self.sw = 0
        self.b1.Hide()
        self.b2.Show()

    def OnSelectImg2(self, event):
        self.sw = 1
        self.b1.Show()
        self.b2.Hide()


class Myapp(wx.App):
    def OnInit(self):
        frame = Myframe(parent=None)
        frame.Show()
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    app = Myapp()
    app.MainLoop()
