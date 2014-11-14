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
import thread
import threading
import random

counter = 0

def semaphore_func(semaphore):
    with semaphore:
        thread_func()
    global counter
    counter -= 1  

def thread_func():
    global counter
    counter += 1
    print "counter: ", counter
    time.sleep(3)

def main():
    max_connection = 5
    semaphore = threading.Semaphore(max_connection) # default is 1
    semaphore.release()
    end_count = 0
    while end_count < 15:
        time.sleep( random.random() * 0.5 + 0.2 )
        with semaphore:
            threading.Thread( target = semaphore_func, args = (semaphore,) ).start()
        end_count += 1

    print "wait for %d threads execution" % counter
    while not counter == 0:
        pass

if __name__ == '__main__':
    main()
