import wx
import sys
from crawler.crawler.spiders import spider
from scrapy.crawler import CrawlerProcess

class elementsWindow(wx.Frame):

    # build an object of the Spider class
    spider = spider.SiteSpider()
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    domain = ''
    url = ''

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
        # define so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

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
        self.Bind(wx.EVT_TEXT, self.OnTypeDomain, id=scannerDomain.GetId())
        hbox1.Add(scannerDomain, proportion=5)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # set the position in the vbox
        vbox.Add((-1, 10))

        # 4th: add new scanner horizontal box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        labelUrl = wx.StaticText(panel, label='Set Url')
        hbox2.Add(labelUrl, flag=wx.RIGHT, border=36)
        scannerUrl = wx.TextCtrl(panel)
        self.Bind(wx.EVT_TEXT, self.OnTypeUrl, id=scannerUrl.GetId())
        hbox2.Add(scannerUrl, proportion=5)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # 5th: build another horizontal box inside the vertical one
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        log = wx.StaticText(panel, label='Log')
        hbox3.Add(log)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        # 6th: add multiple lines
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        logMultiline = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)



        hbox4.Add(logMultiline, proportion=5, flag=wx.EXPAND)
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
        self.Bind(wx.EVT_BUTTON, self.OnStart, id=buttonStart.GetId())
        hbox6.Add(buttonStart)
        buttonSave = wx.Button(panel, label='SAVE', size=(70, 30))
        hbox6.Add(buttonSave, flag=wx.LEFT | wx.BOTTOM, border=5)
        buttonExit = wx.Button(panel, label='EXIT', size=(70, 30))
        buttonExit.Bind(wx.EVT_BUTTON, self.OnQuit, buttonExit)
        hbox6.Add(buttonExit, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # redirection
        sys.stdout = logMultiline

        # set the size of the panel according to the vbox
        panel.SetSizer(vbox)

    # event handling
    def OnTypeDomain(self, e):
        self.domain = e.EventObject.Value

    def OnTypeUrl(self, e):
        self.url = e.EventObject.Value

    def OnStart(self, e):
        self.SetTitle(self.url)
        self.process.crawl(self.spider, start_urls=self.url)
        self.process.start()

    def OnSave(self, e):
        pass

    def OnQuit(self, e):
        self.Close()

# main method
def main():
    app = wx.App(redirect=False)
    elementsWindow(None, title='Demica WebArchiver').Show()
    app.MainLoop()


if __name__ == '__main__':
    main()



