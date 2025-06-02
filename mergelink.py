class Linkedlist:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def middlelist(head):
    if not head:
        return head
    slow,fast=head,head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def merge(left,right):
    if not left:
        return right
    if not right:
        return left
    if left.data <  right.data:
        res=left
        res.next=merge(left.next,right)
    else:
        res=right
        res.next=merge(left,right.next)
    return res


def mergelist(head):
    if not head or not head.next:
        return head

    middle=middlelist(head)
    nexttomiddle=middle.next
    middle.next=None
    left=mergelist(head)
    right=mergelist(nexttomiddle)
    sortedlist=merge(left,right)
    return sortedlist

def printlist(node):
    while node:
        print(node.data,end="-->")
        node=node.next
    print("None")

head=Linkedlist(4)
head.next=Linkedlist(5)
head.next.next=Linkedlist(2)
head.next.next.next=Linkedlist(6)
head.next.next.next.next=Linkedlist(8)
print("----original list-----")
printlist(head)

sortedhead=mergelist(head)

print("----sorted list----")
printlist(sortedhead)



