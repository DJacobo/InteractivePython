# ======================================================== Book Differences
# Don't keep track of the end
#     all add operations will be slower than my version
# Don't keep count of size
#      Their size method iterates through the entire list
# Don't have an initial data value
#     I probably didn't really need to add that either
# Book search and other traversals use "while not found and cur != None"
#     is more readable, and all comparisons happen in the while loop, unlike some of mine
# =========================================================

class MyUnorderedLinkedList():
    def __init__(self, newData=None):
        self.count = 0
        if newData != None:
            self.head = myNode(newData)
            self.count = 1
        else:
            self.head = None
        self.end = self.head

    def addNode(self, newNode):
        if self.isEmpty():
            self.head = newNode
        else:
            self.end.setNext(newNode)
        self.end = newNode
        self.count = self.count + 1

    def addData(self, newData):
        newNode = myNode(newData)
        if self.isEmpty():
            self.head = newNode
        else:
            self.end.setNext(newNode)
        self.end = newNode
        self.count = self.count + 1

    def removeData(self, item):
        prevNode = self.head
        curNode = self.head
        foundItem = False
        while not foundItem and curNode.getData() != item:
            prevNode = curNode
            curNode = curNode.getNext()
            if curNode.getData() == item:
                foundItem = True
                prevNode.setNext(curNode.getNext())
                self.count = self.count - 1

    def search(self, item):
        curNode = self.head
        foundItem = False
        while not foundItem and curNode.getData() != item:
            if curNode.getNext() != None:
                curNode = curNode.getNext()
            else:
                break
        if curNode.getData() == item:
            foundItem = True
        return foundItem

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.count

    # Already handled above
    def append(self, item):
        self.addData(item)

    def index(self, item):
        if self.isEmpty():
            print('list is empty')
            return -1
        cur = self.head
        foundItem = cur.getData() == item
        itemIndex = 0
        while not foundItem and cur.getNext() != None:
            cur = cur.getNext()
            itemIndex = itemIndex + 1
            if cur.getData() == item:
                foundItem = True
        if not foundItem:
            return -1
        return itemIndex

    def insert(self, pos, item):
        newNode = myNode(item)
        prev = self.head
        curIndex = 0
        cur = self.head
        if pos > self.size() or pos < 0:
            # Stop working
            print('%s is not a valid index for a list of size %s' % (pos, self.size()))
        elif pos == 0:
            newNode.setNext(self.head)
            self.head = newNode
            self.count = self.count + 1
        else:
            while curIndex < pos:
                prev = cur
                cur = cur.getNext()
                curIndex = curIndex + 1
            prev.setNext(newNode)
            newNode.setNext(cur)
            self.count = self.count + 1

    def pop(self, index=None):
        pos = 0
        prev = self.head
        cur = self.head
        if index == None:
            index = self.size()-1
        if index < 0:
            print('%s is not a valid index, please select a positive value')
            return None
        elif index > self.size()-1:
            print('%s is too large for a list of size %s' % (index, self.size()-1))
            return None
        while pos < index:
            prev = cur
            cur = cur.getNext()
            pos = pos + 1
        if pos == index:
            if cur != None:
                prev.setNext(cur.getNext())
                if index == 0:
                    self.head = self.head.getNext()
            else:
                prev.setNext(None)
            self.count = self.count - 1
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