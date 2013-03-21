import wx
import  wx.xrc  as  xrc

class MyPanel(wx.Panel):
    
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        # Load the resource
        res = xrc.XmlResource(RESFILE)

        # Now create a panel from the resource data
        panel = res.LoadPanel(self, "MyPanel")


class MainFrame(wx.Frame):
    def __init__(self,
            title="hello world", pos=wx.DefaultPosition,
            size=wx.DefaultSize, 
            style=wx.CAPTION | wx.CLOSE_BOX
            ):

        wx.Frame.__init__(self, None, -1, title, pos, size, style)
        self.createMenuBar()


        panel = wx.Panel(self)
        
        txt = wx.StaticText(panel, -1, "Start after copmuter idle for 10 min.")
        txt.SetPosition((5,5))

        
        button = wx.Button(panel, 1003, "Close Me!")
        button.SetPosition((55, 15))
        self.Bind(wx.EVT_BUTTON, self.OnQuit, button)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)


    def createMenuBar(self):
        MenuBar = wx.MenuBar()

        FileMenu = wx.Menu()
        item = FileMenu.Append(wx.ID_EXIT, text = "&Exit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        item = FileMenu.Append(wx.ID_PREFERENCES, text = "&Preferences")
        self.Bind(wx.EVT_MENU, self.OnPrefs, item)

        #MenuBar.Append(FileMenu, "&File")
        HelpMenu = wx.Menu()
        item = HelpMenu.Append(wx.ID_HELP, "Test &Help",
                                "Help for this simple test")
        self.Bind(wx.EVT_MENU, self.OnHelp, item)

        ## this gets put in the App menu on OS-X
        item = HelpMenu.Append(wx.ID_ABOUT, "&About",
                                "More information About this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, item)
        MenuBar.Append(HelpMenu, "&Help")

        self.SetMenuBar(MenuBar)

        
    def OnQuit(self,Event):
        self.Destroy()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "This is a small program to test\n"
                                     "the use of menus on Mac, etc.\n",
                                "About Me", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnHelp(self, event):
        dlg = wx.MessageDialog(self, "This would be help\n"
                                     "If there was any\n",
                                "Test Help", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, event):
        dlg = wx.MessageDialog(self, "This would be an open Dialog\n"
                                     "If there was anything to open\n",
                                "Open File", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnPrefs(self, event):
        dlg = wx.MessageDialog(self, "This would be an preferences Dialog\n"
                                     "If there were any preferences to set.\n",
                                "Preferences", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
