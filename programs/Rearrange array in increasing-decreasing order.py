#Problem Statement: Rearrange a given array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order

n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))
    
def Selection(arr, n):
    
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

Selection(arr, n)
mid = n // 2
arr[mid:] = arr[mid:][::-1]
print(arr)

'''Output:
Enter size of array: 9
Enter data for index 0: 1
Enter data for index 1: 0
Enter data for index 2: 2
Enter data for index 3: 9
Enter data for index 4: 3
Enter data for index 5: 8
Enter data for index 6: 4
Enter data for index 7: 7
Enter data for index 8: 5
[0, 1, 2, 3, 9, 8, 7, 5, 4]
'''
