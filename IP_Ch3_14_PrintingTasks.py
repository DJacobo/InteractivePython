# Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
# For each second (currentSecond):
#     Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
#     If the printer is not busy and if a task is waiting,
#         Remove the next task from the print queue and assign it to the printer.
#         Subtract the timestamp from the currentSecond to compute the waiting time for that task.
#         Append the waiting time for that task to a list for later processing.
#         Based on the number of pages in the print task, figure out how much time will be required.
#     The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
#     If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
# After the simulation is complete, compute the average waiting time from the list of waiting times generated.

# =================================================================================== My Idea
# main -- loop range(3600) 1 hour
#     Lab
#         tasks = {startTime: endTime, startTime: endTime, etc...}
#         GenerateTask(currentSecond) # 1/180, randomint
#             Assume each page takes one second
#     Task
#         startTime
#         endTime
#         pageCount
#         pagesRemaining
#     printer
#         Q
#         Add
#         Remove
#         isBusy
#         printTask
# =================================================================================== Book Differences
# simulation(numSeconds, PagesPerMinute)  # Allows for more customization of the simulation
#     Queue                               # is part of the simulation, and not the printer itself 
#     printer.startNextTask(task)         # Simulation assigns tasks to printer

# Printer
#     ppm                                 # Doesn't assume 1page/sec, allows change
#     timeRemaining                       # 1s only does as much work as the ppm defines, 60/ppm

# Task
#     waitTimes                           # waitTime called from simulation, before assigning task
# ===================================================================================== Self Check / Extension TODO:
# How would you modify the printer simulation to reflect a larger number of students? Suppose that the number of students was doubled.
# You make need to make some reasonable assumptions about how this simulation was put together but what would you change?
# Modify the code. Also suppose that the length of the average print task was cut in half. Change the code to reflect that change.
# Finally How would you parametertize the number of students, rather than changing the code we would like to make the number of
# students a parameter of the simulation.

from pythonds.basic.queue import Queue
import random

time = 0
waitTimes = []

class Printer():
    def __init__(self):
        self.printQueue = Queue()
        self.currentTask = None

    def isBusy(self):
        return self.currentTask == None

    def addTask(self, task):
        self.printQueue.enqueue(task)

    def removeTask(self):
        self.currentTask = None

    def getNextTask(self):
        if self.printQueue.isEmpty():
            self.currentTask = None
        else:
            self.currentTask = self.printQueue.dequeue()

    def printTask(self):
        if self.currentTask != None:
            self.currentTask.removePage()
            if self.currentTask.isDone():
                self.currentTask = None

        if self.currentTask == None and not self.printQueue.isEmpty():
            self.currentTask = self.printQueue.dequeue()
            waitTimes.append(time - self.currentTask.startTime)

class Task():
    def __init__(self, time, pages):
        self.startTime = time
        self.endTime = 0
        self.pageCount = pages
        self.pagesRemaining = pages

    def removePage(self):
        self.pagesRemaining = self.pagesRemaining-1

    def isDone(self):
        done = False
        if self.pagesRemaining == 0:
            done = True
            self.endTime = time
        return done

    def __str__(self):
        return 'Start: %s, End: %s, Pages: %s' % (self.startTime, self.endTime, self.pageCount)

def willGenerateTask():
    generate = False
    if random.randint(1, 181) == 180:
        generate = True
    return generate

def GenerateTask(time):
    pages = random.randint(1, 21)
    return Task(time, pages)

printer = Printer()
for i in range(3600):
    time = i
    if willGenerateTask():
        newTask = GenerateTask(time)
        printer.addTask(newTask)

    printer.printTask()

totalWait = 0
for instance in waitTimes:
    totalWait = totalWait + instance
print('Average Wait Time: %s' % (totalWait / len(waitTimes)))