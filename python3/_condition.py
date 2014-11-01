#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomomi Yamaguchi
#
# Created:     20/01/2012
# Copyright:   (c) Tomomi Yamaguchi 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import time
import threading

class MyThread(threading.Thread):

    lock = threading.Lock()

    def __init__(self, name, lifetime, condition):
        threading.Thread.__init__(self)
        self.lifetime = lifetime
        self.condition = condition
    def run(self):
        while not self.lifetime <= 0:
            self.lifetime -= 1
            with self.lock:
                time.sleep(0.3)
                print threading.current_thread().getName(), "life is " , self.lifetime
        with self.condition:
            print threading.current_thread().getName(), "acquire"
            self.condition.notify()

def main():
    condition = threading.Condition()
    t1 = MyThread("t1", 5, condition)
    t2 = MyThread("t2", 5, condition)
    t1.start()
    t2.start()
    fact = 0
    while fact < 5:
        with condition:
            condition.wait()
            if not t1.isAlive():
                print "generate thread t1"
                t1 = MyThread("t1_" + str(fact), 5, condition)
                t1.start()
            else:
                print "generate thread t2"
                t2 = MyThread("t1_" + str(fact), 5, condition)
                t2.start()
            fact += 1

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
