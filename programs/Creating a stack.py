 #           ​ Creating a stack:
 
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self):
        x = int(input("Enter the value to push in stack: "))
        self.stack.append(x)
        print(x, " pushed into stack")
        
    def pop(self):
        if not self.stack:
            print("The stack is empty")
        else:
            print("Popped element", self.stack.pop())
    
    def peek(self):
        if not self.stack:
            print("The stack is empty")
        else:
            print("Top element is", self.stack[-1])
            
    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("The stack is", self.stack)

s = Stack()
while True:
    print("---Stack menu---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        s.push()
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")

'''
Output:
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 1
Enter the value to push in stack: 3
3  pushed into stack
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 1
Enter the value to push in stack: 2
2  pushed into stack
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 1
Enter the value to push in stack: 4
4  pushed into stack
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 3
Top element is 4
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 4
The stack is [3, 2, 4]
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 2
Popped element 4
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 4
The stack is [3, 2]
---Stack menu---
1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter your choice: 5
Exiting program
'''
