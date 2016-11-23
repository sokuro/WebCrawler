# to specify the size of the application

import wx

class SizeWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(SizeWindow, self).__init__(*args, **kwargs)

        # InitUI
        self.InitUI()

    # InitUI helping method
    def InitUI(self):
        menubar = wx.MenuBar()

        # create menubar object
        fileMenu = wx.Menu()

        # create menu object  -> Shortcut  -> Name    -> Help String
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        # append the menu item into the menu object
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        # bind the EVT_MENU menu item to the custom OnQuit() method
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        # move the window to the specific px position
        # self.Move((700, 500))

        # set size
        self.SetSize((500, 500))

        # set title
        self.SetTitle('Demica WebArchiver')

        # center the position
        self.Center()
        self.Show(True)

    # helping method to Quit the application
    def OnQuit(self, e):
        self.Close()

# main method
def main():

    ex = wx.App()
    SizeWindow(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()