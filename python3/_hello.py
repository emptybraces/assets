# エンコーディングの指定。１行または２行目に記述された場合にのみ有効
# -*- coding: utf-8 -*-
import sys
# functions
def main():
	# print は3.xでは()で記述する。sys.argvの最初の要素にはファイル名が格納される。
    print(sys.argv);

    # raw string can be invalid escape sequence.
    print("D:\node.py");
    print(r"D:\node.py");

    # pass statement is null operation
    pass;

    # wait user input
    user_input = input("Please enter the key: ");

    # Null Object
    nullObject = None;
    print("true" if nullObject else "false");


# entry point
if __name__ == '__main__':
    main()