#LIFO - Last in, First Out


class Stack():
    def __init__(self):
        self.tab = []
    def is_empty(self):
        if self.tab == [] :
            return True
        return False
    def size(self):
        if self.tab:
            return len(self.tab)
        else :
            return None

    def push(self, item):

        self.tab.append(item)

    def pop(self):
        self.tab.pop()

    def top(self):
        return self.tab[-1]

z = Stack()
z.push(1)
z.push(3)
z.push(7)
print(z.size())
print(z.top())
z.pop()
print(z.size())
print(z.top())
print(z.is_empty())
