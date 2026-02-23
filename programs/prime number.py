#Prime number

n = int(input("Enter the no.: "))
count = 0
if n == 0 or n == 1:
    print(n ,"is a not a prime number")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count > 2:
        print(n ,"is not a prime number")
    else:
        print(n ,"is a prime no.")

'''
Output:
Enter the no.: 5
5 is a prime no.
'''
