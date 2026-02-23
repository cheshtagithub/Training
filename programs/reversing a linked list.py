#Reversing a linked list
# made a class named Node

class Node:
    
    def __init__(self, data):
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
    for i in range(2, n+1):
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
    
    
    # to reverse the linked list
    
    prev = None
    current = head
    
    while current is not None:
        new = current.next  #to store address of next node
        current.next = prev #point to previous element
        prev = current      #prev move forward
        current = new       #current move forward
    head = prev
    
    # to print reversed linked list
    print("The reversed linked list is: ", end = "")
    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print(None)
'''       
    Output:

Enter the number of nodes: 4
Enter the value of data for node number 1: 3
Enter the value of node number 2: 2
Enter the value of node number 3: 5
Enter the value of node number 4: 4
The linked list is: 3-->2-->5-->4-->None
The reversed linked list is: 4-->5-->2-->3-->None
'''
