#Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.
n  = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    a = int(input(f"Enter the first element for index {i}: "))
    b = int(input(f"Enter the second element for index {i}: "))
    arr.append((a, b))
    
print(arr)

for i in range(n):
    for j in range(i + 1,n):
        if arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]:
            print(f"({arr[i][0]}, {arr[i][1]})", end = " ")

'''Output:
Enter the size of array: 8
Enter the first element for index 0: 1
Enter the second element for index 0: 2
Enter the first element for index 1: 2
Enter the second element for index 1: 1
Enter the first element for index 2: 2
Enter the second element for index 2: 3
Enter the first element for index 3: 3
Enter the second element for index 3: 4
Enter the first element for index 4: 4
Enter the second element for index 4: 5
Enter the first element for index 5: 5
Enter the second element for index 5: 4
Enter the first element for index 6: 5
Enter the second element for index 6: 6
Enter the first element for index 7: 6
Enter the second element for index 7: 7
[(1, 2), (2, 1), (2, 3), (3, 4), (4, 5), (5, 4), (5, 6), (6, 7)]
(1, 2) (4, 5)
'''
