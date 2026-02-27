#Problem Statement: Given an array of N integers, the task is to replace each element of the array by its rank in the array.


n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter the element for index {i}: ")))
print(arr)    
unique_no = list(set(arr))
unique_no.sort()
size = len(unique_no)

rank = {}

for i in range(size):
    rank[unique_no[i]] = i + 1
    
result = []
for i in arr:
    result.append(rank[i])
print(*result)

'''Output:
Enter the size of array: 5
Enter the element for index 0: 0
Enter the element for index 1: 2
Enter the element for index 2: 11
Enter the element for index 3: -4
Enter the element for index 4: -9
[0, 2, 11, -4, -9]
3 4 5 2 1
'''
