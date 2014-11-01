# -*- coding: utf-8 -*-
import fileinput
import sys

argc = len(sys.argv)
if argc == 1:
	sys.exit()

# sys.argv[1:]のファイルのコンテンツを列挙
for line in fileinput.input():
	print(line)

for arg in sys.argv:
	print(arg)

#output
# this

# is

# the

# pen.
# this

# is

# the

# apple.