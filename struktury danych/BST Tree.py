class BSTNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None
        self.data = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert_element(self, Node):
        key = Node.key
        curr = self.root
        while curr!= None:
            if key == curr.key:
                return True
            if key > curr.key :
                if curr.right == None:
                    curr.right = Node
                    Node.parent = curr
                    break
                else:
                    curr = curr.right

            if key < curr.key:
                if curr.left == None:
                    curr.left = Node
                    Node.parent = curr
                    break
                else :
                    curr = curr.left

    def search_for_element(self, key):
        curr = self.root
        while curr != None:
            if curr.key == key:
                return curr
            if curr.key < key:
                curr = curr.right
            if curr.key > key:
                curr = curr.left
        return None

    def remove_element(self, key):
        curr = self.search_for_element(key)
        if curr == None:
            return False

        if curr.right == None and curr.left == None:
            if curr.parent.right == curr:
                curr.parent.right = None
                return True
            else:
                curr.parent.left = None
                return True

        if curr.right != None and curr.left == None:
            if curr.parent.right == curr:
                curr.parent.right = curr.right
                return True
            else :
                curr.parent.left = curr.right
                return True

        if curr.right == None and curr.left != None:
            if curr.parent.right == curr:
                curr.parent.right = curr.left
                return True
            else :
                curr.parent.left = curr.left
                return True

        if curr.right != None and curr.left != None:
            successor = self.succ(curr)
            succ_key = successor.key
            self.remove_element(succ_key)
            curr.key = succ_key
            curr.data = successor.data
            return True




    def min(self):
        curr = self.root
        while curr.left != None:
            curr = curr.left
        return curr

    def max(self):
        curr = self.root
        while curr.right != None:
            curr = curr.right
        return curr

    def pred(self, Node):
        curr = Node
        if curr.left != None:
            while curr.right!=None:
                curr = curr.right
            return curr

        if curr.left == None:
            while curr.parent.left == curr:
                curr = curr.parent
            return curr.parent


    def succ(self, Node):
        curr = Node
        if curr.right != None:
            while curr.left != None :
                curr = curr.left
            return curr

        if curr.right == None:
            while curr.parent.right == curr:
                curr = curr.parent
            return curr.parent


