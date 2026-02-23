#            ​ Previous small element
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
n = int(input("Enter the size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter data for {i+1} index: ")))
ans = []
for i in range(n):
    while not s.is_empty() and s.top() >= arr[i]:
        s.pop()
        
    if s.is_empty():
        ans.append(-1)
        
    else:
        ans.append(s.top())
        
    s.push(arr[i])
    
print("previous smaller:", ans)

'''
Output:
Enter the size of array: 5
Enter data for 1 index: 3
Enter data for 2 index: 1
Enter data for 3 index: 0
Enter data for 4 index: 8
Enter data for 5 index: 6
previous smaller: [-1, -1, -1, 0, 0]
'''
