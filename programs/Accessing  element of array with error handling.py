#            ​ Accesing element of array with error handling:
try:
    n = int(input("Enter no. of elements: "))
    
    arr = []
    
    for i in range(n):
        arr.append(int(input(f"Enter the data for index no.{i}: ")))
        
    index = int(input("Enter index to access: "))
    
    print(f"Element at index {index} is: ",arr[index])
    
except ValueError:
    print("Error, please enter valid index")

except IndexError:
    print("Error: Index out of range.")

else:
    print("Access successful.")

finally:
    print("Execution completed.")

"""
Output:
Without error:
Enter no. of elements: 5
Enter the data for index no.0: 7
Enter the data for index no.1: 6
Enter the data for index no.2: 9
Enter the data for index no.3: 8
Enter the data for index no.4: 0
Enter index to access: 3
Element at index 3 is:  8
Access successful.
Execution completed.

With IndexError:
Enter no. of elements: 5
Enter the data for index no.0: 8
Enter the data for index no.1: 7
Enter the data for index no.2: 0
Enter the data for index no.3: 9
Enter the data for index no.4: 6
Enter index to access: 8
ERROR!
Error: Index out of range.
Execution completed.
"""
