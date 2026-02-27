# Problem Statement: Given a 0-indexed integer array nums, find the leftmost equilibrium Index.

n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element for index {i}: ")))

totalSum = sum(arr)

leftSum = 0
rightSum = totalSum
equilibrium_index = -1

for i in range(n):
    rightSum -= arr[i]

    if leftSum == rightSum:
        equilibrium_index = i
        break

    leftSum += arr[i]

if equilibrium_index != -1:
    print("Equilibrium index is:", equilibrium_index)
else:
    print("No equilibrium index found")

'''Output:
Enter the size of array: 6
Enter element for index 0: 2
Enter element for index 1: 3
Enter element for index 2: -1
Enter element for index 3: 8
Enter element for index 4: 4
Enter element for index 5: 0
Equilibrium index is: 3
'''
