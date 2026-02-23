#   Factorial of a no.

# USING RECURSION
n= int(input("Enter the no.: "))
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("factorial of number is", factorial(n))

'''
Output: Enter the no.: 24
factorial of number is 620448401733239439360000
'''

# USING LOOP:
n = int(input("Enter the no.: "))
fact = 1
if n == 0:
    print("factorial of", n , "is", 1)
else:
    for i in range(1,n+1):
        fact *= i
    print("Factorial of ",n ,"is", fact)

'''
Output:
Enter the no.: 5
Factorial of  5 is 120
'''
