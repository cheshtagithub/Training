#            ​ Check if a linked list is palindrome
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
n = int(input("Enter the number of nodes of linked list: "))

if n<= 0:
    print("the linked list is empty")
    
else:
    data = int(input("Enter the value of data for node number 1: "))
    head = Node(data)
    
    current = head
    for i in range(2, n+1):
        data = int(input(f"Enter the value of data for node number {i}: "))
        new_node = Node(data)
        current.next = new_node
        current = new_node
    
    print("The linked list is: ", end = "")
    temp = head
    while temp:
        print(temp.data, end = "-->")
        temp = temp.next
    print("None")
    
    # Divide the linked list in 2 halves
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
     
#Reversing the second half of the linked list   
    prev = None
    curr = slow
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
# Checking if the linked list is palindrome
    first = head
    second = prev
    is_palindrome = True
    
    while second:
        if first.data != second.data:
            is_palindrome = False
        first = first.next
        second = second.next
        
    if is_palindrome == True:
        print("The linked list is palindrome")
    else:
        print("The linked list is not a palindrome")

"""
Output:
Enter the number of nodes of linked list: 5
Enter the value of data for node number 1: 1
Enter the value of data for node number 2: 2
Enter the value of data for node number 3: 3
Enter the value of data for node number 4: 2
Enter the value of data for node number 5: 1
The linked list is: 1-->2-->3-->2-->1-->None
The linked list is palindrome
"""
