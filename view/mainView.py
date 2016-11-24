import wx

class elementsWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(elementsWindow, self).__init__(*args, **kwargs)

        self.InitUI()

        # set size of the panel
        self.SetSize((600, 600))

        # center and show the window
        self.Center()
        self.Show(True)

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

        # 2nd: build a vertical box
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 3rd: build a horizontal box inside the vertical one
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # set a label
        label1 = wx.StaticText(panel, label='Set Domain')
        # label1.SetFont(font)
        # set a scanner right to the static label. Flag and border defines the distance among widgets.
        hbox1.Add(label1, flag=wx.RIGHT, border=10)
        scanner1 = wx.TextCtrl(panel)
        hbox1.Add(scanner1, proportion=5)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # set the position in the vbox
        vbox.Add((-1, 10))

        # 4th: add new scanner horizontal box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label2 = wx.StaticText(panel, label='Set Url')
        hbox2.Add(label2, flag=wx.RIGHT, border=36)
        scanner2 = wx.TextCtrl(panel)
        hbox2.Add(scanner2, proportion=5)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # 5th: build another horizontal box inside the vertical one
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        label3 = wx.StaticText(panel, label='Result')
        hbox3.Add(label3)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        # 6th: add multiple lines
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        scanner3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox4.Add(scanner3, proportion=5, flag=wx.EXPAND)
        vbox.Add(hbox4, proportion=5, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 10))

        # 7th: generate the output file


        # 8th: add some buttons
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        button1 = wx.Button(panel, label='START', size=(70, 30))
        hbox6.Add(button1)
        button2 = wx.Button(panel, label='SAVE', size=(70, 30))
        hbox6.Add(button2, flag=wx.LEFT | wx.BOTTOM, border=5)
        button3 = wx.Button(panel, label='EXIT', size=(70, 30))
        button3.Bind(wx.EVT_BUTTON, self.OnQuit, button3)
        hbox6.Add(button3, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # set the size of the panel according to the vbox
        panel.SetSizer(vbox)

    def OnQuit(self, e):
        self.Close()

def main():
    app = wx.App()
    elementsWindow(None, title='Demica WebArchiver')
    app.MainLoop()


if __name__ == '__main__':
    main()



