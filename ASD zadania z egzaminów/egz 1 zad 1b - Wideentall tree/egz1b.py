from egz1btesty import runtests

def height_check(curr_node, height):
    if curr_node != None:
        curr_node.x = height
        return max(height_check(curr_node.left, height + 1), height_check(curr_node.right, height + 1))
    return height


def travel(curr, levels):
    if curr != None:
        levels[curr.x] += 1
        travel(curr.left, levels)
        travel(curr.right, levels)

def cutting_below(curr, height, cuts):
    if curr.x == height :
        if curr.left :
            cuts[0] +=1
            curr.left = None
        if curr.right :
            cuts[0] += 1
            curr.right = None
    if curr.right:
        cutting_below(curr.right, height, cuts)
    if curr.left :
        cutting_below(curr.left, height, cuts)

def retag_x(curr, height, cuts):
    if curr == None:
        return 0
    if curr.right == None and curr.left == None:
        return curr.x
    curr.x = max(retag_x(curr.left, height, cuts), retag_x(curr.right, height, cuts))
    return curr.x

def cut_rest(curr, height, cuts):
    if curr != None :
        if curr.x < height :
            cuts[0] +=1
            return 0
        cut_rest(curr.left, height, cuts)
        cut_rest(curr.right, height, cuts)





class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    height = height_check(T, 0)
    levels = [0 for i in range(height)]
    travel(T, levels)
    maximum = max(levels)
    n = len(levels)
    height = 0
    for i in range(n-1, -1, -1):
        if levels[i] == maximum:
            height = i
            break

    cuts = [0]
    cutting_below(T, height, cuts)
    retag_x(T, height, cuts)
    cut_rest(T, height, cuts)
    return cuts[0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )