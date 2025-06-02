from queue import Queue

class StackQueue:
    def __init__(self):
        self.q = Queue()

    def push(self, value):
        size = self.q.qsize()  # Corrected: q.qsize() instead of q.size()
        self.q.put(value)
        for _ in range(size):
            self.q.put(self.q.get())  # Rotating the queue to simulate stack behavior

    def pop(self):
        if self.q.empty():
            return -1
        return self.q.get()

    def top(self):
        if self.q.empty():
            return -1
        return self.q.queue[0]  # Accessing the front element in the queue (top of stack)

    def empty(self):
        return self.q.empty()

    def printstack(self):
        return list(self.q.queue)  # Corrected: returns the queue as a list to view its contents

# Example Usage
s = StackQueue()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.printstack())  # Output: [40, 30, 20, 10]
