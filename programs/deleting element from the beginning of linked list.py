#      Deleting element from the start of linked list

class Node:

    def __init__(self,data):
        self.data = data
        self.next =None

n = int(input("Enter the number of nodes:"))

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
    print("The linked list is:",end="")

    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")

    print("After deleting node from the beginning the new linked list will be: ", end = "")
    head = head.next
    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")

'''
Output:
Enter the number of nodes: 5
Enter the data of first node, node1: 4
Enter the data for node number 2: 7
Enter the data for node number 3: 6
Enter the data for node number 4: 3
Enter the data for node number 5: 2
The linked list is: 4-->7-->6-->3-->2-->None
After deleting node from the beginning the new linked list will be: 7-->6-->3-->2-->None
'''
