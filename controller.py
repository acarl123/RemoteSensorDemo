import wx
import flask
from threading import Thread
import random # testing only

import plotfix as plot
from view import MainFrame


class MainController:
    def __init__(self, inputQ):
        self.mainWindow = MainFrame(None)
        self.inputQ = inputQ

        self.mainWindow.Bind(wx.EVT_MENU, self.onExit, self.mainWindow.menuExit)
        self.mainWindow.Bind(wx.EVT_MENU, self.toggleStart, self.mainWindow.menuStartStop)
        self.mainWindow.Bind(wx.EVT_TIMER, self.update, self.mainWindow.timerUpdate)

        self.mainWindow.m_statusBar1.SetStatusText('Not Running')

        self.running = False
        self.data = []

    def show(self):
        self.mainWindow.Show()

    def onExit(self, event):
        exit()

    def toggleStart(self, event):
        if not self.running:
            self.start()
        else:
            self.stop()

        self.running = not self.running

    def start(self):
        self.mainWindow.timerUpdate.Start(2000)
        self.mainWindow.menuStartStop.SetItemLabel('Stop')
        self.data = []
        self.mainWindow.plotter.Clear()
        self.mainWindow.m_statusBar1.SetStatusText('Waiting for connection...')

    def stop(self):
        self.mainWindow.timerUpdate.Stop()
        self.mainWindow.menuStartStop.SetItemLabel('Start')
        self.mainWindow.m_statusBar1.SetStatusText('Not Running')


    def update(self, event):
        if self.inputQ.empty():
           self.mainWindow.m_statusBar1.SetStatusText('Waiting for connection...')
           return
        # data = random.randint(20,40)
        data = float(eval(self.inputQ.get()).rstrip())
        if data > 100: return
        self.data.append(data)
        line = plot.PolyLine([(index*2, item) for index, item in enumerate(self.data)], legend='', colour='blue', width=2)
        gc = plot.PlotGraphics([line], 'Temperature', 'Time (s)', 'Temperature')
        self.mainWindow.plotter.Draw(gc, xAxis=(0, len(self.data)+5), yAxis=(0, max(self.data)+5))
        self.mainWindow.m_statusBar1.SetStatusText('Last recorded value: %s' % data)