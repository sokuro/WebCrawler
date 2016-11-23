import wx

class elementsWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(elementsWindow, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        # build a menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        # 1st: build a panel
        panel = wx.Panel(self)

        # font = wx.SytemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        # font.SetPointSize(12)

        # 2nd: build a vertical box
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 3rd: build a horizontal box inside the vertical one
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # set a label
        label1 = wx.StaticText(panel, label='Set Domain')
        # label1.SetFont(font)
        # set a scanner right to the static label
        hbox1.Add(label1, flag=wx.RIGHT, border=10)
        scanner1 = wx.TextCtrl(panel)
        hbox1.Add(scanner1, proportion=5)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        # 4th: build another horizontal box inside the vertical one
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label2 = wx.StaticText(panel, label='Result')
        hbox2.Add(label2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        # 5th: add multiple lines
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        scanner2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(scanner2, proportion=5, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=5, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 10))

        # 6th: add some buttons
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        button1 = wx.Button(panel, label='OK', size=(70, 30))
        hbox5.Add(button1)
        button2 = wx.Button(panel, label='EXIT', size=(70, 30))
        hbox5.Add(button2, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # set the size of the panel according to the vbox
        panel.SetSizer(vbox)

        # set size of the panel
        self.SetSize((600, 600))

        # center and show the window
        self.Center()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

def main():
    app = wx.App()
    elementsWindow(None, title='Demica WebArchiver')
    app.MainLoop()


if __name__ == '__main__':
    main()



