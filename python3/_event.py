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
import thread
import threading

end_count = 3

def thread_func(event, counter):
    time.sleep(2)
    while len(counter) < end_count:
        while not event.isSet():
            print "wait result: ", event.wait(1)
        print "counter : %d" % len(counter)
        counter.append("")
        event.clear()

def main():
    event = threading.Event()
    counter = []
    print thread.get_ident()
    print thread.start_new_thread( thread_func, (event, counter) )
    while len(counter) < end_count:
        event.set()
        time.sleep(2)

if __name__ == '__main__':
    main()
