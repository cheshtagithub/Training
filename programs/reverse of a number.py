#Reverse of a number

 n = int(input("Enter the number: "))
def reverse(n, sum):
    if n == 0:
        return sum
    else:
        a = n % 10
        sum = sum * 10 + a
        return reverse(n//10, sum)
print("Reverse of number ",n ,"is:" ,reverse(n,0))

'''
Output:
Enter the number:89
Reverse of number  89 is: 98

USING LOOP'''

n = int(input("Enter the no.: "))
sum = 0
Temp = n
while Temp > 0:
      a = Temp % 10
      sum = sum * 10 + a
      Temp = Temp//10
print("reverse of ",n ,"is", sum)

'''
Output:Enter the no.:9876
reverse of  9876 is 6789
'''
