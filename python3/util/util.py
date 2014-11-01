import sys
import os
from inspect import stack

def log(message, output=""):
	caller_frame = stack()[1];
	try :
		print("{} :{}, {}".format(
			message,
			os.path.basename(caller_frame[1]),
			caller_frame[2]));
	finally:
		del caller_frame;
def convertStringList2IntList(stringList):
    return list(map(lambda x: int(x), stringList));

def filterForOnly(func, iter, missingMessage = ""):
    lst = list(filter(func, iter));
    assert lst, missingMessage;
    return lst[0];

