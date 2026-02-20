 #     Adding element at the beginning or end of linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input("Enter the number of nodes: "))
if n <= 0:
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

    print("The linked list is: ", end = "")

    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")

    data_loc = int(input("Enter where to add new node , if at beginning write 0 or write 1 for end: "))
    data = int(input("enter the data to be added: "))
    new = Node(data)

    if data_loc == 0:
        new.next = head
        head = new

    elif data_loc == 1:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new

    else:
        print("Invalid choice")


    print("The new linked list after adding the data is: ", end = "" )
    temp = head
    while temp is not None:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")

"""    
Output:
# to add data at beginning

Enter the number of nodes: 5
Enter the data of first node, node1: 9
Enter the data for node number 2: 0
Enter the data for node number 3: 8
Enter the data for node number 4: 7
Enter the data for node number 5: 6
The linked list is: 9-->0-->8-->7-->6-->None
Enter where to add new node , if at beginning write 0 or write 1 for end: 0
enter the data to be added: 2
The new linked list after adding data is: 2-->9-->0-->8-->7-->6-->None

# to add data at end

Enter the number of nodes: 4
Enter the data of first node, node1: 0
Enter the data for node number 2: 8
Enter the data for node number 3: 7
Enter the data for node number 4: 9
The linked list is: 0-->8-->7-->9-->None
Enter where to add new node , if at beginning write 0 or write 1 for end: 1
enter the data to be added: 4
The new linked list after adding the data is: 0-->8-->7-->9-->4-->None
"""
