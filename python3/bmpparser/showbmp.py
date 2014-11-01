#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      maximilian
#
# Created:     19/01/2012
# Copyright:   (c) maximilian 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import threading
import time
import bmpparser
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt

class Worker(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.bmp = bmpparser.BitmapParser()
        self.window = window

    def run(self):
        self.bmp.load("./data/kp2.bmp")
        print self.bmp.fh
        print self.bmp.ih
        self.window.showComponents(False)

class Progress(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.worker = Worker(self)
        self.worker.setDaemon(True)


        self.bar = QtGui.QProgressBar(self)
        self.bar.setRange(0, 0)
        self.bar.setGeometry(0, 125, 400, 50)

        self.button = QtGui.QPushButton("test", self)
        self.button.setGeometry(0, 0, 100, 30)
        self.button.clicked.connect(self.pushed)

        self.statusBar()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Bitmap perser')

    def pushed(self):
        self.worker.start()

    def paintEvent(self, e):

        if not self.worker.bmp.isLoadFinished:
            return

        w = self.worker.bmp.ih.data["width"]
        h = self.worker.bmp.ih.data["height"]
        p = QtGui.QPainter(self)
        p.begin(self)
        for y in range(h):
            for x in range(w):
                p.setPen( QtGui.QColor( self.worker.bmp.g.data[ y ][ x ] ) )
                p.drawPoint(x, y)
        p.end()

    def showComponents(self, isShow):
        self.button.setShown(isShow)
        self.bar.setShown(isShow)
        self.resize( self.worker.bmp.ih.data["width"], self.worker.bmp.ih.data["height"] )

def main():
    app = QtGui.QApplication(sys.argv)
    p = Progress()
    p.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
