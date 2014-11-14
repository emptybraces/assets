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
    #lock = threading.RLock()

    def __init__(self, name, lifetime):
        threading.Thread.__init__(self)
        self.lifetime = lifetime
        #self.name = name
    def run(self):
        while not self.lifetime <= 0:
            self.lifetime -= 1
            self.lock.acquire()
            # self.lock.acquire() # when use RLock
            print threading.current_thread().getName(), "life is " , self.lifetime
            self.lock.release()
            # self.lock.release() # # when use RLock
            # RuntimeError gasousyutusarerukoro
            time.sleep(0.3)


def main():

    t1 = MyThread("t1", 5)
    t2 = MyThread("t2", 5)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
