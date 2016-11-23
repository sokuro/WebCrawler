# warmUp: a simple small window example

# imports: core, controls, GDI, misc, windows
import wx

# creates an application object. Each wxPython program must have one!
app = wx.App()

# wx.Frame widget as a container widget (parent for all other widgets).
# None indicates no parent
frame = wx.Frame(None, -1, 'simple.py')
frame.Show()

# mainloop: endless cycle. It catches & dispatches all events that exists during the life of the application
app.MainLoop()



