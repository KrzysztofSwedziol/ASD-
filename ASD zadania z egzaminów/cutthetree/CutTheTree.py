from Exercise_2_tests import runtests
from math import inf


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutter(curr):
    if curr.left == None and curr.right == None:
        return inf
    curr_min_left = inf
    curr_min_right = inf
    if curr.left != None and (curr.left.left != None or curr.left.right != None):
        curr_min_left = curr.left.value
    if curr.left == None :
        curr_min_left = 0
    if curr.right != None and (curr.right.left != None or curr.right.right != None):
        curr_min_right = curr.right.value
    if curr.right == None:
        curr_min_right = 0

    curr_min = curr_min_left + curr_min_right

    if curr.left != None:
        curr_min_left = min(curr_min_left, cutter(curr.left))
    if curr.right != None:
        curr_min_right = min(curr_min_right, cutter(curr.right))
    if curr_min_left + curr_min_right < curr_min:
        curr_min = curr_min_left + curr_min_right
    return curr_min


def cutthetree(T):
    minimum = cutter(T)
    return minimum

runtests(cutthetree)