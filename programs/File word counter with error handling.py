#            ​ File word counter

try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        print("Number of words:", len(words))

except FileNotFoundError:
    print("File not found. Please check the file name.")

except PermissionError:
    print("You do not have permission to access this file.")

finally:
    print("Program ended.")

'''
Output:
Enter file name: File word counter with error handling.py 
Number of words: 54
Program ended.
'''
