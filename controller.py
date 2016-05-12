import wx
import flask
from threading import Thread

from view import MainFrame


class MainController:
    def __init__(self, inputQ):
        self.mainWindow = MainFrame(None)

    def show(self):
        self.mainWindow.Show()
