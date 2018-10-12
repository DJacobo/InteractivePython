class MyOrderedList():
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, item):
        newNode = myNode(item)
        if self.isEmpty() or self.head.getData() > item:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            prev = self.head
            cur = self.head
            while cur != None and cur.getData() < item:
                prev = cur
                cur = cur.getNext()
            newNode.setNext(cur)
            prev.setNext(newNode)
        self.count = self.count + 1

    def remove(self, item):
        prev = self.head
        cur = self.head
        foundItem = False
        if self.isEmpty() or self.head.getData() > item:
            # item does not exist in the list
            foundItem = False
            # raise IndexError('item does not exist in the list')
        else:
            while not foundItem and cur != None:
                if cur.getData() < item:
                    prev = cur
                    cur = cur.getNext()
                elif cur.getData() == item:
                    foundItem = True
                elif cur.getData() > item:
                    cur = None
        if foundItem:
            prev.setNext(cur.getNext())
            self.count = self.count - 1
        else:
            raise IndexError('%s does NOT exist in the list' % (item))

    def search(self, item):
        prev = self.head
        cur = self.head
        foundItem = False
        if self.isEmpty() or self.head.getData() > item:
            # item does not exist in the list
            foundItem = False
        else:
            while not foundItem and cur != None:
                if cur.getData() < item:
                    prev = cur
                    cur = cur.getNext()
                elif cur.getData() == item:
                    foundItem = True
                elif cur.getData() > item:
                    cur = None
        return foundItem
            

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.count

    def index(self, item):
        prev = self.head
        cur = self.head
        curIndex = 0
        foundItem = False
        if self.isEmpty() or self.head.getData() > item:
            foundItem = False
        else:
            while not foundItem and cur != None:
                if cur.getData() < item:
                    prev = cur
                    cur = cur.getNext()
                    curIndex = curIndex + 1
                elif cur.getData() == item:
                    foundItem = True
                else:
                    cur = None
        if not foundItem:
            curIndex = -1
        return curIndex
             
    def pop(self, pos=None):
        if pos == None:
            pos = self.size()-1
        elif self.isEmpty() or pos > self.size()-1:
            raise IndexError('Index does not exist in the list')
        prev = self.head
        cur = self.head
        curIndex = 0
        while curIndex < pos:
            cur = cur.getNext()
            curIndex = curIndex + 1
        self.count = self.count-1
        return cur.getData()

class myNode():
    def __init__(self, newData=None):
        self.data = newData
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, newNode):
        self.next = newNode

# newList = MyOrderedList()
# newList.add(1)
# newList.add(2)
# newList.add(31)
# newList.add(77)
# newList.add(17)
# newList.add(93)
# newList.add(26)
# newList.add(54)

# print(newList.size())
# print(newList.search(31))
# print(newList.search(32))
# print(newList.search(0))

# cur = newList.head
# for i in range(newList.size()):
#     print(cur.getData())
#     cur = cur.getNext()

# newList.remove(31)
# cur = newList.head
# for i in range(newList.size()):
#     print(cur.getData())
#     cur = cur.getNext()

# newList.remove(1000)