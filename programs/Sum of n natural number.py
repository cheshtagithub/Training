#Sum of n natural number

n = int(input("Enter the no.: "))
sum = 0
if n < 0:
    print("invalid number")
else:
    for i in range(n + 1):
        sum += i
    print("Sum of first", n ,"natural number is", sum)
    
'''
Output:
Enter the no.:5
Sum of first 5 natural number is 15

With error handling:'''

try:
    n = int(input("Enter the no.: "))
    sum = 0
    if n < 0:
        raise ValueError("The value of n is negative,")
    for i in range(n + 1):
        sum += i
    print("Sum of first", n ,"natural number is", sum)
except ValueError as e:
    print(e,"Enter a valid integer.")
    
'''
Output:
When enter negative integer
Enter the no.: -9
The value of n is negative, Enter a valid integer.
When enter invalid data
Enter the no.: ddddd
invalid literal for int() with base 10: 'ddddd' Enter a valid integer.
'''
