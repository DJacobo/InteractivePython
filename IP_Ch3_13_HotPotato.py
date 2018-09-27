# Assume that the child holding the potato will be at the front of the queue.
# Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child, putting her at the end of the line.
# She will then wait until all the others have been at the front before it will be her turn again.
# After num dequeue/enqueue operations, the child at the front will be removed permanently and another cycle will begin.
# This process will continue until only one name remains (the size of the queue is 1).
from pythonds.basic.queue import Queue

def hotPotato(num, names):
    potatoQueue = Queue() 
    for name in names:
        potatoQueue.enqueue(name)

    while potatoQueue.size() > 1:
        for i in range(num):
            potatoQueue.enqueue(potatoQueue.dequeue())
        potatoQueue.dequeue()
    return potatoQueue.dequeue()

kids = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
print(hotPotato(5, kids))