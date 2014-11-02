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
def convertElementType(iterator, func):
    """convert type of element to specified type."""
    return list(map(lambda x: func(x), iterator));

def filterForOnly(func, iter, missingMessage = ""):
    lst = list(filter(func, iter));
    assert lst, missingMessage;
    return lst[0];

def normalize(values):
    """ normalize vector3 """
    x = values[0];
    y = values[1];
    z = values[2];
    length = x*x + y*y + z*z;
    out = [x, y, z];
    if length > 0:
        length = 1 / math.sqrt(length);
        out[0] = x * length;
        out[1] = y * length;
        out[2] = z * length;
    return out;
