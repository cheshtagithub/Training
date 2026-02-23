#Making linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(19)
node2 = Node(23)
node3 = Node(87)
node4 = Node(99)

node1.next = node2
node2.next = node3
node3.next = node4

print("The linked list is: ", end = "")
current = node1
while current:
    print(current.data, end = "-->")
    current = current.next
print("None")

'''
Output:
The linked list is: 19-->23-->87-->99-->None
'''
