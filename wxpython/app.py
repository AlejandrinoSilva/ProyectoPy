import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 600))
        self.Centre()
        # Se crea el panel
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.label = wx.StaticText(self, label="Hello World", style=wx.ALIGN_CENTER)
        vbox.Add(self.label, 0, wx.EXPAND)
        self.label2 = wx.StaticText(self, label="Hello World", style=wx.ALIGN_CENTER)
        hbox.Add(self.label2, 0, wx.EXPAND)
        vbox.Add(hbox)

        self.SetSizer(vbox)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Sistemas RamSys S.A.")
        self.frame.Show()
        return True

if __name__=="__main__":
    app = MyApp()
    app.MainLoop()
