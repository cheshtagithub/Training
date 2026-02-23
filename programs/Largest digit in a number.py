#       Largest digit in a number

n = int(input("Enter the no.: "))
max_no = 0
Temp = n
while Temp > 0:
      a = Temp%10
      if a > max_no:
          max_no = a
      Temp = Temp//10
print("the largest digit in ",n ,"is", max_no)

'''
OUTPUT:
Enter the no.: 9878
the largest digit in  9878 is 9
'''
