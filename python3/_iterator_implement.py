# -*- coding: utf-8 -*-
import sys

class Fib:                                        
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                           
        self.a = 0
        self.b = 1
        return self

    def __next__(self):                           
        fib = self.a
        if fib > self.max:
            raise StopIteration                   
        self.a, self.b = self.b, self.a + self.b
        return fib

# function definition
def main():
    for i in Fib(10):
        print(i)

# entry point
if __name__ == '__main__':
    main()