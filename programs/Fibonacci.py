#    Fibonacci series
n = int(input("Enter the number: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("the series is: ")
for i in range(n):
    print(fibonacci(i))

'''
Output: Enter the number: 7
the series is:
0
1
1
2
3
5
8
'''
