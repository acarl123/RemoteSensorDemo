# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import plotfix as plot


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.menuExit = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.menuExit)

        self.m_menubar1.Append(self.m_menu1, u"File")

        self.m_menu2 = wx.Menu()
        self.menuStartStop = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Start", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.AppendItem(self.menuStartStop)

        self.m_menubar1.Append(self.m_menu2, u"Test")

        self.SetMenuBar(self.m_menubar1)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.plotter = plot.PlotCanvas(self. wx.ID_ANY, )

        bSizer1.Add(self.plotter, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.timerUpdate = wx.Timer()
        self.timerUpdate.SetOwner(self, wx.ID_ANY)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


