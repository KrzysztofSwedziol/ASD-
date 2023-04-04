#FIFO - First in First out

class queue():
    def __init__(self):
        self.tab = []
    def size(self):
        return len(self.tab)
    def is_empty(self):
        if len(self.tab) == 0 :
            return True
        return False
    def push(self, item):
        self.tab.append(item)
    def pop(self):
        for i in range(len(self.tab)-1):
            self.tab[i]=self.tab[i+1]
        del self.tab[len(self.tab)-1]
    def top(self):
        return self.tab[0]

l = queue()
l.push(1)
l.push(3)
l.push(7)
print(l.size())
print(l.is_empty())
print(l.top())
l.pop()
print(l.size())
print(l.top())
