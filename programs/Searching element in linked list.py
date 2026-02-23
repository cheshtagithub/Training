#Searching element in linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

n = int(input("Enter the number of nodes: "))
if n <= 0:
    print("The linked list is empty")

else:
    data = int(input("Enter the data of first node, node1: "))
    head = Node(data)

    current = head
    for i in range(2, n + 1):
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

    key = int(input("Enter the element to be searched: "))
    temp = head
    index = 1
    found = False

    while temp is not None:
        if key == temp.data:
            print("The element is present at index:", index)
            found = True
            break
        temp = temp.next
        index += 1
    if not found:
        print("Not found")
 
'''       
    Output:
Enter the number of nodes: 3
Enter the data of first node, node1: 2
Enter the data for node number 2: 3
Enter the data for node number 3: 4
The linked list is: 2-->3-->4-->None
Enter the element to be searched: 5
Not found
'''
