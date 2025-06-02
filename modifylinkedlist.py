class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def appendlist(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=newnode
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def rearrangelist(self):
        if not self.head or not self.head.next:
            return None
        oddlist=Node(0)
        evenlist=Node(0)
        eventail=evenlist
        oddtail=oddlist
        curr=self.head
        while curr:
            if curr.data % 2==0:
                eventail.next=curr
                eventail=eventail.next
            else:
                oddtail.next=curr
                oddtail=oddtail.next
            curr=curr.next
        oddtail.next=None
        eventail.next=oddlist.next
        self.head=evenlist.next

ll=Linkedlist()
data=[3,1,0,2,4,6]
for num in data:
    ll.appendlist(num)
print("Original list")
ll.printlist()
ll.rearrangelist()
print("After the arranging")
ll.printlist()


