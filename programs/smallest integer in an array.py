#Find the smallest element in an array

n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))

min_element = arr[0]

for i in range(n):
    if min_element > arr[i]:
        min_element = arr[i]

print("the smallest integer in the array is: ",min_element)

''' Output:
Enter the size of array: 6
Enter data for index 0: 88
Enter data for index 1: 77
Enter data for index 2: 66
Enter data for index 3: 2
Enter data for index 4: 9
Enter data for index 5: 0
the smallest integer in the array is:  0
'''
