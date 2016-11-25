import wx

class elementsWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(elementsWindow, self).__init__(*args, **kwargs)

        self.InitUI()

        # set size of the panel
        self.SetSize((700, 700))

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
        # bind the method to the event
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        # 1st: build a panel
        panel = wx.Panel(self)

        # 2nd: build a vertical box
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 3rd: build a horizontal box inside the vertical one
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # set a label
        labelDomain = wx.StaticText(panel, label='Set Domain')
        # label1.SetFont(font)
        # set a scanner right to the static label. Flag and border defines the distance among widgets.
        hbox1.Add(labelDomain, flag=wx.RIGHT, border=10)
        scannerDomain = wx.TextCtrl(panel)
        hbox1.Add(scannerDomain, proportion=5)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # set the position in the vbox
        vbox.Add((-1, 10))

        # 4th: add new scanner horizontal box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        labelUrl = wx.StaticText(panel, label='Set Url')
        hbox2.Add(labelUrl, flag=wx.RIGHT, border=36)
        scannerUrl = wx.TextCtrl(panel)
        hbox2.Add(scannerUrl, proportion=5)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # 5th: build another horizontal box inside the vertical one
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        labelResult = wx.StaticText(panel, label='Result')
        hbox3.Add(labelResult)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        # 6th: add multiple lines
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        scannerMultiline = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox4.Add(scannerMultiline, proportion=5, flag=wx.EXPAND)
        vbox.Add(hbox4, proportion=5, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 10))

        # 7th: generate the output file
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        labelOutput = wx.StaticText(panel, label='Output File')
        hbox5.Add(labelOutput, flag=wx.RIGHT, border=20)
        scannerOutput = wx.TextCtrl(panel)
        hbox5.Add(scannerOutput, proportion=5)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=10)

        vbox.Add((-1, 10))

        # 8th: add some buttons
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        buttonStart = wx.Button(panel, label='START', size=(70, 30))
        hbox6.Add(buttonStart)
        buttonSave = wx.Button(panel, label='SAVE', size=(70, 30))
        hbox6.Add(buttonSave, flag=wx.LEFT | wx.BOTTOM, border=5)
        buttonExit = wx.Button(panel, label='EXIT', size=(70, 30))
        buttonExit.Bind(wx.EVT_BUTTON, self.OnQuit, buttonExit)
        hbox6.Add(buttonExit, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # set the size of the panel according to the vbox
        panel.SetSizer(vbox)

    # event handling
    def OnStart(self, e):
        pass

    def OnSave(self, e):
        pass

    def OnQuit(self, e):
        self.Close()

# main method
def main():
    app = wx.App()
    elementsWindow(None, title='Demica WebArchiver')
    app.MainLoop()


if __name__ == '__main__':
    main()



