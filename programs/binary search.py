 #       Binary search
# to input array from the user
n = int(input("Enter value of n: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("array is", arr)
#to sort array before binary search
def selection(arr):
    x = len(arr)
    for i in range(x-1):
        min_ind = i
        for j in range(i+1, x):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
       # to display sorted array
selection(arr)
print("After sorting array is", arr)

key = int(input("Enter element to search: "))
# binary search code
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element", key ,"is found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid – 1

"""
Output:
Enter value of n: 5
9
7
5
0
2
array is [9, 7, 5, 0, 2]
After sorting array is [0, 2, 5, 7, 9]
Enter element to search: 5
Element 5 is found at index 2
"""
