# -*- coding: utf-8 -*-
import sys
import os
import shutil
import glob


def main():

	cur_file 	= os.path.basename(sys.argv[0])
	cur_dir 	= os.path.dirname(sys.argv[0])
	
	#----- change current directory 
	#os.chdir(path)
	
	#----- get current directory
	#os.getcwd()
	
	#----- return a list containing the names of the entries in the directory given by path
	#for files in os.listdir(os.path.dirname(cur_file)):
		# must be checked fullpath
	#	print files, " is directory" if os.path.isdir(os.path.join(cur_dir, files)) else files
		
	#----- create a directory named path with numeric mode mode. default mode is 0777(octal)
	#os.mkdir( os.path.join(cur_dir, "SampleDirectory" ) )
	
	#----- Recursive directory creation function
	#os.makedirs( os.path.join(cur_dir, r"SampleDirectories/a/b/c/d/e") )
	
	#----- remove the file path.cannot remove directory
	#os.remove( os.path.join(cur_dir, r"SampleDirectory" ) )
	
	#----- remove the directory
	#os.rmdir( os.path.join(cur_dir, r"SampleDirectory" ) )
	
	#----- remove directories recursively.
	# cannot remove non empty directiry
	#os.removedirs( os.path.join(cur_dir, r"SampleDirectories/a/b/c/d/e" ) )
	# all removes 
	#shutil.rmtree( os.path.join(cur_dir, r"SampleDirectories"), 1 )
	
	#----- return a possibly-empty list of path names that match pathname
	# >>> glob.glob('./[0-9].*')
	# ['./1.gif', './2.txt']
	# >>> glob.glob('*.gif')
	# ['1.gif', 'card.gif']
	# >>> glob.glob('?.gif')
	# ['1.gif']
	#for list in glob.glob(os.path.join(cur_dir, r"*bat") ):
	#	print list
	
	#----- copy the contents of the file named stc to a file named dst.
	src = os.path.join(cur_dir, cur_file)
	dst = os.path.join(cur_dir, "SampleDirectories" )
	#shutil.copy(src, dst)
	#----- recursive copy directories
	shutil.copytree( os.path.join(cur_dir, r"SampleDirectories"), os.path.join(cur_dir, "aaa") )
	
	#----- move the contents of the file named stc to a file named dst.
	#shutil.move(src, dst)
	
	
	
	
	
	
	
if __name__ == '__main__':
	main()