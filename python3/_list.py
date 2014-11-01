import sys
# function definition
def main():
    # array size
    size = 3;
    # 1 dimentional
    d1 = [True for i in range(size)];  
    print(d1);
    # 2 dimentional
    d2 = [[0, 0] for i in range(size)]
    print(d2);

# entry point
if __name__ == '__main__':
    main()