import wx
from flask import Flask, request
from flask.ext.api import status
from controller import MainController
import Queue
import thread

inputQ = Queue.Queue()
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', defaults={'path': ''},methods=['POST'])
@app.route('/<path:path>',methods=['POST'])
def main(path, *args, **kwargs):
    inputQ.put(request.data)
    return request.data, status.HTTP_200_OK

if __name__ == '__main__':
    wxapp = wx.App()
    controller = MainController(inputQ)
    controller.show()
    app.debug = False
    thread.start_new(app.run, tuple(), {'host' : '192.168.173.1'})
    wxapp.MainLoop()