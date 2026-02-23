'''            ​ Disarium number: 
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Example: # 75
--> 7^1 + 5^2 = 7 + 25 = 32 
--> Not disarium'''

n = input("Enter the string of number: ")
n_int = int(n)
index = 1
sum = 0
for i in range(len(n)):
    int_n = int(n[i])
    sum = sum + int_n ** index
    index += 1
if n_int == sum:
    print("The given number is disarium number")
else:
    print("The given number is not disarium number")

'''
Output:
Enter the string of number: 135
The given number is disarium number
'''
