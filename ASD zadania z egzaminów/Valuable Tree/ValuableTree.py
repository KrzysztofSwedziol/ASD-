class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.x = None

root = Node()
root.leftval = 1
root.rightval = 5
root.x = 1
B = Node()
root.left = B
B.x = 2
E = Node()
E.x = 5
root.right = E
B.leftval = 6
B.rightval = 2
D = Node()
D.x = 4
B.left = D
C = Node()
C.x = 3
B.right = C
C.leftval = 8
C.rightval = 10
F = Node()
F.x = 6
C.left = F
G = Node()
G.x = 7
C.right = G

def how_much(curr, nodes):
    if curr != None:
        nodes.append(curr)
        how_much(curr.left, nodes)
        how_much(curr.right, nodes)


def travel(curr, k, maximum, memo):
    curr_val = maximum
    copy_curr = curr_val
    if k == 0:
        return maximum
    if curr == None:
        return 0
    if memo[k][curr.x] != 0:
        return memo[k][curr.x]

    for i in range(k + 1):
        if i > 0 and k-i > 0:
            curr_val = copy_curr + travel(curr.left, i-1, curr.leftval, memo) + travel(curr.right, k-i-1, curr.rightval, memo)
        if i == 0:
            curr_val = copy_curr + travel(curr.right, k-1, curr.rightval, memo)
        if k-i == 0:
            curr_val = copy_curr + travel(curr.left, i-1, curr.leftval, memo)
        if curr_val > maximum:
            maximum = curr_val
            curr_val = copy_curr

    memo[k][curr.x] = maximum
    return maximum

def ValuableTree(tree, k):
    maximum = 0
    nodes = []
    how_much(tree, nodes)
    memo = [[0 for i in range(len(nodes) + 1)] for j in range(k + 1)]
    for i in nodes:
        curr = travel(i, k, 0, memo)
        if curr > maximum:
            maximum = curr

    return maximum

print(ValuableTree(root, 3))


