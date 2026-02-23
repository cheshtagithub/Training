#            ​ Valid parentheses

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


s = Stack()
n = input("Enter the string of parentheses: ")

pairs = {')': '(', '}': '{', ']': '['}
valid = True

for ch in n:

    if ch in "({[":
        s.push(ch)


    elif ch in ")}]":
        if not s.stack:
            valid = False
            break

        top = s.pop()
        if top != pairs[ch]:
            valid = False
            break


if valid and not s.stack:
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")

'''
Output:
Enter the string of parentheses: {{[()]}}
Valid Parentheses
'''
