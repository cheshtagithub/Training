#Find the largest element in an array

n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))

large = arr[0]

for i in range(n):
    if large < arr[i]:
        large = arr[i]

print("the largest integer in the array is: ",large)

'''Output:
Enter the size of array: 5
Enter data for index 0: 0
Enter data for index 1: 9
Enter data for index 2: 10
Enter data for index 3: 22
Enter data for index 4: 56
the largest integer in the array is:  56
'''
