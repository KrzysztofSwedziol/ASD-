class BST_Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None
        self.data = None

class BST:
    def __init__(self, first_value):
        self.root = BST_Node
        self.root.key = first_value

    def print_tree(self, curr): #the function goes as far to the right as pozzible and then makes turns
        if curr.key == None:
            print(None)
        if curr.key != None:
            print(curr.key)
            self.print_tree(curr.right)
            self.print_tree(curr.left)

    def search(self, value):
        curr = self.root
        while(curr!=None):
            if curr.key < value:
                curr = curr.right
            if curr.key > value :
                curr = curr.left
            if curr.key == value:
                return curr.key
        return None

    def insert(self, value):
        new = BST_Node
        new.key = value
        curr = self.root
        shadow = curr
        while curr!= None:
            if curr.key < value:
                shadow = curr
                curr = curr.right
            if curr.key > value :
                shadow = curr
                curr = curr.left
            if curr.key == value:
                return True
        if value > shadow.key :
            shadow.right = new
            new.parent = shadow
        if value < shadow.key :
            shadow.left = new
            new.parent = shadow

    def remove(self, Node):
        if Node.left == None and Node.right == None :
            if Node.parent.right == Node:
                Node.parent.right = None
            if Node.parent.left == Node:
                Node.parent.left = None
        if Node.left == None and Node.right != None:
            if Node.parent.right == Node :
                Node.parent.right = Node.right
            if Node.parent.left == Node:
                Node.parent.left = Node.right
        if Node.right == None and Node.left != None :
            if Node.parent.right == Node :
                Node.parent.right = Node.left
            if Node.parent.left == Node :
                Node.parent.left = Node.left
        if Node.left != None and Node.right != None :
            a = self.successor(Node)
            if Node.left != None:
                a.left = Node.left
            Node = a


    def minimum(self):
        curr = self.root
        shadow = curr
        while curr != None:
            shadow = curr
            curr = curr.left
        return shadow.key

    def maximum(self):
        curr = self.root
        shadow = curr
        while curr != None:
            shadow = curr
            curr = curr.right
        return shadow.key

    def predecessor(self, Node):
        if Node.left == None:
            shadow = Node
            curr = Node
            while curr.parent.right == curr :
                shadow = curr
                curr = curr.parent

            return curr.parent

        if Node.left != None:
            searcher = Node.left
            shadow = Node.left
            while searcher != None :
                shadow = searcher
                searcher = searcher.right
            return shadow

    def successor(self, Node):
        if Node.right == None:
            shadow = Node
            curr = Node
            while curr.parent.right == curr:
                shadow = curr
                curr = curr.parent
            return curr.parent

        if Node.right != None:
            searcher = Node.right
            shadow = Node.right
            while searcher != None:
                shadow = searcher
                searcher = searcher.left
            return shadow

tree = BST(10)
tree.print_tree(tree.root)


