from array import *

def middle(lst):
    lst.pop()
    lst.remove(lst[0])
    return lst