"""

"""
from collections import deque


class Queue:
    # Dunder function.
    def __init__(self, l=[]):
        self.qUEUE = deque(l)

    def size(self):
        return len(self.qUEUE)

    def peek(self):
        return self.qUEUE[-1]

    def push(self, value):
        return self.qUEUE.appendleft(value)

    def pop(self, value):
        return self.qUEUE.pop(), self.qUEUE

    def isEmpty(self):
        return len(self.qUEUE) == 0

    def __str__(self):
        s = ""
        x1 = len(self.qUEUE)
        for i in range(x1):
            s = s + str(self.qUEUE[i])+"\n"
        s = "\n"+s
        return s


l = [11, 24, 3, 72, 51, 23]
a = Queue(l)
print(a)
