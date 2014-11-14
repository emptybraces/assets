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
import threading


def f():
    print "hello world delay"

class MyThread:
    def run(self):
        print "hello from class"

def main():
    t1 = threading.Timer(3.0, f)
    t2 = threading.Timer(4.0, MyThread().run )
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
