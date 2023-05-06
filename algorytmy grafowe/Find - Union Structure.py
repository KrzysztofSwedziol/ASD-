class Node:
    def __init__(self, value):
        self.parent = self
        self. value = value
        self.rank = 0


def findset(node):
    if node.parent != node:
        node.parent = findset(node.parent)

    return node.parent



def union(set1, set2):
    set1 = findset(set1)
    set2 = findset(set2)
    if set1.rank > set2.rank:
        set2.parent = set1
    else :
        set1.parent = set2
        if set1.rank == set2.rank:
            set2.rank+=1
