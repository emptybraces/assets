#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      maximilianahead
#
# Created:     20/01/2012
# Copyright:   (c) maximilianahead 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import time
import threading

class MyThread(threading.Thread):

    lock = threading.Lock()

    def __init__(self, name, lifetime):
        threading.Thread.__init__(self)
        self.lifetime = lifetime
        #self.name = name
    def run(self):
        while not self.lifetime <= 0:
            self.lifetime -= 1
            self.lock.acquire()
            print threading.current_thread().getName(), "life is " , self.lifetime
            self.lock.release()
            self.lock.release()
            time.sleep(0.3)


def main():

    t1 = MyThread("t1", 5)
    t2 = MyThread("t2", 5)
    t1.start()
    t2.start()
    #print threading.enumerate()
    #print len(threading.enumerate())
    print threading.activeCount()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
