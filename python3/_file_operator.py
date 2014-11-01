# -*- coding: utf-8 -*-
import sys
import os


def main():
	# common variable
	path = r"xxx/yyy/zzz.txt"
	env_path = r"%PATH%"
	user_path = r"~home"
	same_prefix_pathlist = [r"aaa1.txt", r"aaa2.txt", r"aaa3.txt"]
	
	#----- return a normalized absoluted version of the path
	# D:\works\Python\xxx\yyy\zzz.txt
	#print os.path.abspath(path)
	
	#----- return the base name of path
	# zzz.txt
	#print os.path.basename(path)
	
	#----- return the longest path prefix
	# aaa
	#print os.path.commonprefix(same_prefix_pathlist)
	
	#----- return the directory path 
	# xxx/yyy
	#print os.path.dirname(path)
	
	#----- file exists
	# False
	#print os.path.exists(path)
	
	#----- return the argument with an initial component of ["] or ["user] replaced by that user's home directory
	# C:\Users\home
	#print os.path.expanduser(user_path)
	
	#----- return the argument with environment variables expanded
	#        On Wiondows, %name% expansions  are supported in addition to $name and ${name}
	# C:\Program Files\Common Files\...;...
	#print os.path.expandvars(env_path)
	
	#----- return the time of last access of path (a seconds)
	# 1340579405.04
	#try:
	#	print os.path.getatime(sys.argv[0])
	#except( os.error ):
	#	print "illegal access"
	
	#----- return the time of last modification of path(a seconds)
	# 1340585397.22
	#try:
	#	print os.path.getmtime(sys.argv[0])
	#except:
	#	print "illegal access"
	
	#----- return the system's ctime which, on some systems(like Unix) is the time of the last change,
	#        and, on others(like Windows), is the creation time for path.
	# 1340579405.04
	#try:
	#	print os.path.getctime(sys.argv[0])
	#except:
	#	print "illegal access"
	
	#----- return the size, in byte
	# 1859
	#print os.path.getsize(sys.argv[0])
	
	#----- return True if path is an absolute pathname
	# True
	#print os.path.isabs(os.path.abspath(sys.argv[0]))
	
	#----- return True if path is an existing regular file.
	# True
	#print os.path.isfile(sys.argv[0])
	
	#----- return True path is an existing durectory.
	# False
	#print os.path.isdir(sys.argv[0])
	
	#----- return True if path refers to a directory entry that is a sysbolic link.
	#
	#os.path.islink(path)
	
	#----- join one or more path components intelligently.
	# abc\def
	#print os.path.join("abc", "def")
	
	#----- normalize a pathname. 
	#         this collapses redundant separators and up-level references so that
	#         A//B, A/B/, A/./B and A/foo/../B all become A/B.
	# A\B
	#print os.path.normpath("A/foo/../B")
	
	#----- normalize the case of a pathname
	# directory/test.txt
	#print os.path.normcase("DIRECTORY/TEST.TXT")
	
	#----- return the canonical path of the specified filename
	# D:\works\Python\file_operator.py
	#print os.path.realpath(sys.argv[0])
	
	#----- return a relative filepath to path either from the current directory or from oprional start point
	# y\z.txt
	#print os.path.relpath(r"x/y/z.txt", r"x")
	
	#----- return True if both pathname arguments refer to the same file or directory
	#
	#print os.path.samefile(sys.argv[0], sys.argv[0])
	
	#----- split the pathname path int oa pair, (head, tail) 
	#        where tail is the last pathname component and head is everything leading up to that,
	# ('D:\\works\\Python', 'file_operator.py')
	#print os.path.split(os.path.abspath(sys.argv[0]))
	
	#----- split the pathname path into a pair(drive, tail) where drive is either a drive specification or the empty string.
	# ('D:', '\\works\\Python\\file_operator.py')
	#print os.path.splitdrive(os.path.abspath(sys.argv[0]))
	
	#----- split the pathname path into a pair(root, ext) such that root + ext == path, and ext, is empty
	#         or begins with a period and contains at most one period.
	# ('D:\\works\\Python\\file_operator', '.py')
	#print os.path.splitext(os.path.abspath(sys.argv[0]))
	
	#----- split the pathname path into a pair (unc, rest) so that unc is the UNC mount point(such as r'\\host\mount'), 
	#         if present, and rest the rest of the path(such as r'path\file.ext')
	#
	#print os.path.splitunc(r"\\host\mount\a\b\c\test.txt")
	
	#----- calls the function visit with arguments(arg, dirname, names) for each directory in the directory
	#        tree rooted at path(including path itself, if it is a directory). 
	#        The argument dirname specifies the visited directory, the argument names lists the files in the directory (gotten from os.listdir(dirname)).
	#        Note:This function is deprecated and has been removed in Python 3 in favor of os.walk().
	#
	
	
	
	
	
	
	
	
	
	
	




if __name__ == '__main__':
	main()
