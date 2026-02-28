#Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

min_val = int(input("Enter minimum value: "))
max_val = int(input("Enter maximum value: "))

for i in range(min_val, max_val + 1):
    reverse = 0
    temp = i

    # Reverse the number
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10

    # Check palindrome
    if i == reverse:
        print(i, end=" ")

'''Output:
Enter minimum value: 4
Enter maximum value: 58
4 5 6 7 8 9 11 22 33 44 55 
'''
