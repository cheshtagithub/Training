#     Deleting element from nth node in linked list
# made a class named Node

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
n = int(input("Enter the number of nodes: "))
if n <= 0:
     print("The linked list is empty")

# to input data in the linked list
else:
    data = int(input("Enter the value of data for node number 1: "))
    head = Node(data)
    
    current = head
    for i in range(2,n+1):
        data = int(input(f"Enter the value of node number {i}: "))
        new_node = Node(data)
        current.next = new_node
        current = new_node
        
    #  to print the linked list
    print("The linked list is: ", end = "")
    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")
    
    
    # to delete element at given node
    node_number = int(input("Enter the number of the node that you want to remove: "))
    temp = head
    index = 1
    while temp is not None:
        if index == node_number - 1:
            temp.next = temp.next.next
        temp = temp.next
        index += 1
    #to print linked list after deleting the element
    print("The linked list after deleting the element is: ", end = "")
    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")

'''
Output:
Enter the number of nodes: 5
Enter the value of data for node number 1: 4
Enter the value of node number 2: 3
Enter the value of node number 3: 6
Enter the value of node number 4: 8
Enter the value of node number 5: 9
The linked list is: 4-->3-->6-->8-->9-->None
Enter the number of the node that you want to remove: 3
The linked list after deleting the element is: 4-->3-->8-->9-->None
'''
