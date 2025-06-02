class Queuewithstack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def isempty(self):
        return len(self.stack1)==0
    def enque(self,ele):
        self.stack1.append(ele)
    def dequeue(self):
        if not self.stack1 and self.stack2:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    