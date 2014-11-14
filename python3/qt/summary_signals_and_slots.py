# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 14:37:30 2012

@author: maximilianahead
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QWidget, QPushButton, QApplication
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot

class Foo(QObject):
    # This defines a signal called 'closed' that takes no arguments.
    closed = pyqtSignal()
    trigger = pyqtSignal()

    # This defines a signal called 'rangeChanged' that takes two
    # integer arguments.
    range_changed = pyqtSignal(int, int, name='rangeChanged')

    # This defines a signal called 'valueChanged' that has two overloads,
    # one that takes an integer argument and one that takes a QString
    # argument.  Note that because we use a string to specify the type of
    # the QString argument then this code will run under Python v2 and v3.
    valueChanged = pyqtSignal([int], ['QString'])
    
    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.
        print "trigger signal received"
        
class ConnectingSignals(QWidget):
    def __init__(self):
        super(ConnectingSignals, self).__init__()
        self.case1()
        self.case2()
        self.case3()
        
    def case1(self):
        but = QtGui.QPushButton("Case1", self)
        but.clicked.connect(self.on_clicked)
        but.move(0, 0)
        
    def case2(self):
        but = QPushButton("Case2", self, clicked = self.on_clicked)
        but.move(80, 0)
        
    def case3(self):
        but = QPushButton("Case3", self)
        but.pyqtConfigure(clicked = self.on_clicked)
        but.move(160, 0)
       
    def on_clicked(self):
        print "clicked"
        

class Decorator():
    @pyqtSlot()
    def foo(self):
        """ C++: void foo() """

    @pyqtSlot(int, str)
    def foo(self, arg1, arg2):
        """ C++: void foo(int, QString) """

    @pyqtSlot(int, name='bar')
    def foo(self, arg1):
        """ C++: void bar(int) """

    @pyqtSlot(int, result=int)
    def foo(self, arg1):
        """ C++: int foo(int) """

    @pyqtSlot(int, QObject)
    def foo(self, arg1):
        """ C++: int foo(int, QObject *) """

class ConectingSlotByName(QWidget):
    def __init__(self):
        super(ConectingSlotByName, self).__init__()
        spinbox = QtGui.QSpinBox(self)
        spinbox.on_spinbox_valueChanged.connect(self.on_spinbox_valueChanged)
    def on_spinbox_valueChanged(self):
        print "on_spinbox_valueChanged"
        

        
        
class CustomSpinBox(QtGui.QSpinBox):
    def on_spinbox_valueChanged(self):
        print "on"

     
        
    
def main():
    #f = Foo()
    #f.connect_and_emit_trigger()
    
    app = QApplication(sys.argv)
    w = ConectingSlotByName()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
