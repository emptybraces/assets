#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      maximilianahead
#
# Created:     10/04/2012
# Copyright:   (c) maximilianahead 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import struct


# 	<	リトルエンディアン(インテル系)
#	>	ビッグエンディアン(モトローラ系)
#	c	char
#	b	char	(integer)
# 	h	short
# 	i	int
# 	f	float
# 	d	double

def main():
	path = 'data/test1.bin'
	# write
	with open(path, 'wb' ) as f:
		f.write( struct.pack( '<5i', 100, 200, 300, 400, 500) );
		
	#read
	with open(path, 'rb' ) as f:
		data = struct.unpack('b',  f.read(0x01 ) );
		print(data)
		data = struct.unpack('b', f.read(0x01) );
		print(data)
	
	

if __name__ == '__main__':
    main()
