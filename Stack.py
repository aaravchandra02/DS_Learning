"""
deque - Doubly Ended Queue; deque provides an O(1) time complexity for append and pop 
operations as compared to list which provides O(n) time complexity.
"""
from collections import deque


class Stack:
    def __init__(self, l=[]):
        self.sTACK = deque(l)

    def enqueue(self, value):
        self.sTACK.append(value)

    def dequeue(self):
        return self.sTACK.pop(), self.sTACK

    def peek(self):
        return self.sTACK[-1]

    def size(self):
        return len(self.sTACK)

    def isEmpty(self):
        return len(self.sTACK) == 0

    # It is used to giving a final representation to the end user.
    def __str__(self):
        s = ""
        x1 = len(self.sTACK)
        for i in range(x1):
            s = str(self.sTACK[i])+"\n"+s
        s = "\n"+s
        return(s)


l = [11, 24, 3, 72, 51, 23]
a = Stack(l)
print(a)
