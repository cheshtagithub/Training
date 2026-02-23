#     Deleting element from the end of linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next =None

n = int(input("Enter the number of nodes: "))

if n<=0:
    print("The linked list is empty")
else:
    data = int(input("Enter the data of first node, node1: "))
    head = Node(data)

    current = head
    for i in range(2, n+1):
        data = int(input(f"Enter the data for node number {i}: "))
        new_node = Node(data)
        current.next = new_node
        current = new_node
    print("The linked list is:", end = "")

    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")

    print("After deleting node from the end, the new linked list will be:", end="")
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None

    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")
 
 '''   
Output:
Enter the number of nodes: 5
Enter the data of first node, node1: 4
Enter the data for node number 2: 3
Enter the data for node number 3: 8
Enter the data for node number 4: 7
Enter the data for node number 5: 6
The linked list is: 4-->3-->8-->7-->6-->None
After deleting node from the end, the new linked list will be: 4-->3-->8-->7-->None
'''
