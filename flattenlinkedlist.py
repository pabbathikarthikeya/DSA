class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None



def flatten(root):
    if not root:
        return None
    res=[]
    curr=root
    while curr:
        bottom_curr=curr
        while bottom_curr:
            res.append(bottom_curr.data)
            bottom_curr=bottom_curr.bottom
        curr=curr.next
    res.sort()
    dummy=Node(0)
    curr=dummy
    for val in res:
        curr.bottom=Node(val)
        curr=curr.bottom
    return dummy.bottom
        
    



def print_flattened_list(node):
    while node:
        print(node.data, end=" ")
        node = node.bottom
    print()

def build_linked_list(arr):
    head = None
    prev = None

    for sublist in arr:
        if not sublist:
            continue
        main_node = Node(sublist[0])
        if not head:
            head = main_node
        if prev:
            prev.next = main_node
        prev = main_node

        bottom_prev = main_node
        for val in sublist[1:]:
            new_node = Node(val)
            bottom_prev.bottom = new_node
            bottom_prev = new_node
    return head

# 🧾 Example input: list of sub-linked-lists
arr = [
    [5, 7, 8, 30],
    [10, 20],
    [19, 22, 50],
    [28, 35, 40, 45]
]

# 🛠️ Build the 2D linked list
root = build_linked_list(arr)

# 🔃 Flatten the linked list
flattened = flatten(root)

# 📤 Print the flattened linked list
print("Flattened linked list is:")
print_flattened_list(flattened)
