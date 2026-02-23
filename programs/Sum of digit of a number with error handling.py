#Sum of digit of a number

try:
    x = int(input("Enter the number: "))
    def summation(x):
        sum = 0
        if x == 0:
            return 0
        else:
            a = x % 10
            sum = sum + a
            b = x//10
           
        return sum + summation(b)
    print("sum of digit of ",x ,"is", summation(x))
    
except ValueError:
    print("Enter integer please")

'''
Output:
Enter the number:876
sum of digit of  876 is 21
'''
