# Implementing a deque with a list means that adding and removing from rear are O(n) operations
class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(len(self.items), item)
    
    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.addRear(4)
print(d)
d.addRear('dog')	
print(d) 
d.addFront('cat')
print(d)
d.addFront(True)
print(d)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d)
print(d.removeRear())
print(d)
print(d.removeFront())
print(d)