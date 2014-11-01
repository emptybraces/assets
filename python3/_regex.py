# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:59:23 2012

@author: Tomomi Yamaguchi

meta characters 
. 改行以外の任意の1文字
* 0回を含める繰り返し
+ 1回以上の繰り返し
? 0回か1回の２つを限定する繰り返し
{m, n} m回以上、n回以下の繰り返し 省略可能、省略した場合、0或いは無限


 ^ $ * + ? { [ \ | ( )
\d
数字とマッチ。クラス [0-9]と同義
\D
数字以外とマッチ。クラス [^0-9]& と同義
\s
あらゆる空白文字とマッチ。クラス [ \t\n\r\f\v] と同義
\S
空白文字以外のあらゆる文字とマッチ。クラス [^ \t\n\r\f\v] と同義
\w
英数字とマッチ。クラス [a-zA-Z0-9_] と同義
\W
英数字以外のあらゆる文字とマッチ。クラス [^a-zA-Z0-9_]と同義

コンパイル時フラグ
IGNORECASE, I	大文字小文字を区別しない
LOCALE, L	      ロケールを考慮してマッチングを行う
MULTILINE, M	複数行にマッチング。これは ^ と $ に影響する
DOTALL, S	      . が改行も含めて、全ての文字とマッチするように指定する
VERBOSE, X	     冗長な正規表現（もっと、きれいで分かりやすくまとめられる表現）を有効にする。
"""


import re

def main():
    p = re.compile("[a-z]+")
    print p
    m = p.match("tempo")
    print m.group()
    print m.start(), m.end()
    print m.span()
    
    
if __name__ == '__main__':
    main()
