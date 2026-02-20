  #          ​ Censoring a string by replacing asked charactes with *
            ​    
n = input("Enter the string of number: ")
y = input("enter the ch you want to censor: ")
for ch in y:
    n = n.replace(ch, "*")
print(n)

"""
Output:
Enter the string of number: Hello, Good morning everyone.Today is a pretty day.
enter the ch you want to censor: loet
H****, G**d m*rning *v*ry*n*.T*day is a pr***y day.
"""
