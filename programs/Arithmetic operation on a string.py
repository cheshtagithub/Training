 #           ​ Arithmetic operation on a string
n = input("Enter the string of number: ")
a, op, b = n.split()
a = int(a)
b = int(b)
if op == "+":
    print("After arithmetic calculation on string the result is: " ,a + b)
elif op == "-":
    print("After arithmetic calculation on string the result is: " ,a - b)
elif op == "*":
    print("After arithmetic calculation on string the result is: " ,a * b)
elif op == "/":
    if b == 0:
        print("Invalid Divisor, so result is:", -1)
    print("After arithmetic calculation on string the result is: " ,a // b)    

"""
Output:
Enter the string of number: 12 + 45
After arithmetic calculation on string the result is:  57
"""
