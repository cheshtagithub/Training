#     Code to print * pattern
#1. 
n = int(input("Enter value of n: "))
for i in range(1, n+1):
	for j in range(1, n+1):
    	print("*", end = " ")
	print()

""" Output:
Enter value of n: 3
* * *
* * *
* * *  
"""
#2.
n = int(input("Enter value of n: "))
for i in range(1, n+1):
	for j in range(i):
    	print("*", end = " ")
	print()

"""Output:
Enter value of n: 5
*
* *
* * *
* * * *
* * * * *
"""
#3.
n = int(input("Enter value of n: "))
for i in range(1, n+1):
	for j in range(n+1, i, -1):
    	print("*", end = " ")
	print()

"""Output:
Enter value of n: 5
* * * * *
* * * *
* * *
* *
*
"""

#4.
n = int(input("enter value of n: "))
for i in range(1, n+1):
	print(" " *  (n - i) , "* " * i)

"""Output: 
enter value of n: 5
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
"""
#5.
n = int(input("Enter value of n: "))
for i in range(1, n+1):
    print(" " * i , "* " * (n - i + 1))

"""Output:
Enter value of n:5
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
"""
