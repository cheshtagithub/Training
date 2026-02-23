#            ​ ZeroDivisionError: 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print("Result is:", result)

finally:
    print("Execution completed")

'''
Output:
Without Error
Enter first number: 88
Enter second number: 8
Result is: 11.0
Execution completed
With ZeroDivisionError:
Enter first number: 99
Enter second number: 0
ERROR!
Error: Cannot divide by zero.
Execution completed
'''
