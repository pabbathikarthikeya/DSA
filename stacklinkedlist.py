class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head=newnode
        else:

            newnode.next=self.head
            self.head=newnode
    def insertatend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newnode
    def insertatmiddle(self,data,index):
        if index==0:
            self.insertatbegin(data)
        pos=0
        curr=self.head
        while curr!=None and pos+1!=index:
            curr=curr.next
            pos=pos+1
        if curr!=None:
            newnode=Node(data)
            newnode.next=curr.next
            curr.next=newnode
    def deleteatbegin(self):
        if self.head==None:
            return
        self.head=self.head.next
    def deleteatend(self):
        if self.head==None:
            return
        curr=self.head
        while curr.next!=None and curr.next.next!=None:
            curr=curr.next
        curr.next=None
    def deleteatmiddle(self,index):
        if self.head==None:
            return
        pos=0
        curr=self.head
        while curr!=None and pos+1!=index:
            pos+=1
            curr=curr.next
        if curr.next==None and curr.next.next==None:
            print("No index")
        else:
            curr.next=curr.next.next

    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next

ll=Linkedlist()
ll.insertatbegin(1)
ll.insertatend(4)
ll.insertatbegin(2)
ll.insertatmiddle(3,2)
ll.deleteatbegin()
ll.deleteatend()
ll.insertatmiddle(4,2)
ll.insertatmiddle(5,2)
ll.insertatmiddle(6,2)
ll.deleteatmiddle(2)
ll.deleteatmiddle(3)
ll.printlist()
