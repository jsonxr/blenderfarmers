#!/usr/bin/env python

import wx
from wx import xrc
import os

#---------------------------------------------------------------------------



class Application(wx.App):
    
    def __init__(self, *args, **kwargs):
        wx.App.__init__(self, *args, **kwargs)
        
        # This catches events when the app is asked to activate by some other
        # process
        self.Bind(wx.EVT_ACTIVATE_APP, self.OnActivate)

    def resourcePath(self, filename):
        if '_MEIPASS2' in os.environ:
            path = os.path.join(os.environ["_MEIPASS2"], filename)
        else:
            path = filename
        return path

    def OnInit(self):
        gui = self.resourcePath('resources/gui.xrc')

        self.res = xrc.XmlResource(gui)
        self.InitFrame()
        self.InitMenu()
        
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
        
    def InitFrame(self):    
        self.frame = self.res.LoadFrame(None, 'mainFrame')
        
        favicon = wx.Icon(self.resourcePath('resources/blenderfarmers.ico'))
        self.frame.SetIcon(favicon)
        
        self.panel = xrc.XRCCTRL(self.frame, 'panel')
        self.txtUrl = xrc.XRCCTRL(self.panel, 'txtUrl')
        self.frame.Bind(wx.EVT_BUTTON, self.OnSubmit, id=xrc.XRCID('btnSubmit'))

    def InitMenu(self):
        self.menuBar = self.res.LoadMenuBar("menuBar")
        
        # The help menu goes here so the "About" goes in the right place on a mac.
        HelpMenu = wx.Menu()
        HelpMenu.Append(wx.ID_HELP, "BlenderFarmer Help",
                                "Help for this simple test")

        ## this gets put in the App menu on OS-X
        HelpMenu.Append(wx.ID_ABOUT, "&About",
                                "More information About this program")
        self.menuBar.Append(HelpMenu, "&Help")
        
        self.frame.Bind(wx.EVT_MENU, self.OnHelp, id=wx.ID_HELP)
        self.frame.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        self.frame.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_EXIT)
        #self.frame.Bind(wx.EVT_MENU, self.Add, id=xrc.XRCID("AddMenuItem"))
        self.frame.SetMenuBar(self.menuBar)
        
    def BringWindowToFront(self):
        try: # it's possible for this event to come when the frame is closed
            self.GetTopWindow().Raise()
        except:
            pass

    def OnActivate(self, event):
        # if this is an activate event, rather than something else, like iconize.
        if event.GetActive():
            self.BringWindowToFront()
        event.Skip()
        
    def MacReopenApp(self):
            """Called when the doc icon is clicked, and ???"""
            self.GetTopWindow().Raise()
#---------------------------------------------------------------------------

    def OnQuit(self,Event):
        self.frame.Destroy()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self.frame, "Popup About Window.\n",
                                "About Me", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnHelp(self, event):
        dlg = wx.MessageDialog(self.frame, "This will go to website help page.\n",
                                "Test Help", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnSubmit(self, event):
            dlg = wx.MessageDialog(self.frame, "Congrats.  You clicked a button." + self.txtUrl.GetValue(),
                                    "Button Click", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        

#---------------------------------------------------------------------------



if __name__ == '__main__':
    application = Application()
    application.MainLoop()
