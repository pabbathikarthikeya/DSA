class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.isempty():
            return None
        popped=self.top.data
        self.top=self.top.next
        return popped
    def peek(self):
        return self.top.data
    def printstack(self):
        curr=self.top
        while curr:
            print(curr.data)
            curr=curr.next

s=Stack()
s.push(10)
s.push(20)
s.push(30)
peeks=s.peek()
poppppp=s.pop()
print("Peeked value",peeks)
print("Popped val",poppppp)
s.printstack()
