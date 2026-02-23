#Palindrome number

n = int(input("Enter the no.: "))
sum = 0
Temp = n
while Temp > 0:
      a = Temp % 10
      sum = sum * 10 + a
      Temp = Temp//10
if sum == n:
    print(n ,"is a palindrome no.")
else:
    print(n ,"is not a palindrome no.")

'''
Output:
Enter the no.: 98767
98767 is not a palindrome no.
'''
