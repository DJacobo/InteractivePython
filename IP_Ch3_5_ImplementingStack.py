# Use a list to hold the stack
# the end of the list will hold the top element of the stack

class MyStack():
    def __init__(self):
        self.data = []

    def isEmpty(self):
        # return len(self.data) == 0
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

def revString(word):
    reverse = ''
    stack = MyStack()
    for c in word:
        stack.push(c)
    while not stack.isEmpty():
        reverse = reverse + str(stack.pop())
    return reverse

print(revString('abcdefghijklmnopqrstuvwxyz'))

# s=MyStack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())