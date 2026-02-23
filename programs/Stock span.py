#            ​ Stock span

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
price_len = int(input("Enter the number of days when stock price is taken: "))

price = []
for i in range(price_len):
    price.append(int(input(f"Enter price for day {i+1}: ")))
ans = []

for i in range(price_len):
    while not s.is_empty() and price[s.top()] <= price[i]:
        s.pop()
        
    if s.is_empty():
        ans.append(i + 1)
        
    else:
        ans.append(i - s.top())
        
    s.push(i)
print("stock span:", ans)

'''
Output:
Enter the number of days when stock price is taken: 5
Enter price for day 1: 2
Enter price for day 2: 4
Enter price for day 3: 1
Enter price for day 4: 3
Enter price for day 5: 6
stock span: [1, 2, 1, 2, 5]
'''
