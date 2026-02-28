#Problem Statement: Given a number N, print the smallest and largest digits present in the number.


n = int(input("Enter a number: "))

maxDigit = 0
minDigit = 9

while n > 0:
    digit = n % 10

    if digit > maxDigit:
        maxDigit = digit

    if digit < minDigit:
        minDigit = digit

    n = n // 10

print("Max Digit:", maxDigit)
print("Min Digit:", minDigit)

'''Output:
Enter a number: 78438648327985340971632613028743
Max Digit: 9
Min Digit: 0
'''
