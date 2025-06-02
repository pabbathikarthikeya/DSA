class Queue:
    def __init__(self,maxsize):
        self.items=[]
        self.maxsize=maxsize
    def enque(self,data):
        if not self.isfull():
            self.items.append(data)
    def deque(self):
        if not self.isempty():
            return self.items.pop(0)
    def isfull(self):
        return len(self.items)==self.maxsize
    def isempty(self):
        return len(self.items)==0
    def size(self):
        return self.len(self.items)
    def printqueue(self):
        print(self.items)
q=Queue(maxsize=10)
q.enque(3)
q.enque(4)
q.enque(5)
q.enque(6)
q.enque(7)
q.enque(8)
q.deque()
q.enque(9)
q.deque()

q.printqueue()

