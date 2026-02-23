#           ​ Next greater:
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()
            
    def top(self):
        return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0


s = Stack()
arr_len = int(input("Enter the number of element in array: "))

arr = []
for i in range(arr_len):
    arr.append(int(input(f"Enter data for index {i+1}: ")))
next_greater = []

for i in range(arr_len - 1, -1, -1):
    while not s.is_empty() and s.top() <= arr[i]:
        s.pop()
        
    if s.is_empty():
        next_greater.append(-1)
        
    else:
        next_greater.append(s.top())
        
    s.push(arr[i])
    
next_greater.reverse()
print("Next greater of the elements in the array are", next_greater)

'''
Output:
Enter the number of element in array: 5
Enter data for index 1: 6
Enter data for index 2: 8
Enter data for index 3: 0
Enter data for index 4: 1
Enter data for index 5: 3
Next greater of the elements in the array are [8, -1, 1, 3, -1]
'''
