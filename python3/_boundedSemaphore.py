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

def main():

    max_connection = 5
    semaphore = threading.BoundedSemaphore(max_connection) # default 1
    try:
        semaphore.release()
    except ValueError:
        print("error");
        return;

if __name__ == '__main__':
    main()
