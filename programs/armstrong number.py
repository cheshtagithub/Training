#Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.


number = int(input("Enter a number: "))

k = len(str(number))   # Number of digits
sum = 0
n = number

while n > 0:
    a = n % 10        
    sum += a ** k     
    n = n // 10

if sum == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

'''Output:
Enter a number: 153
153 is an Armstrong number.
'''
