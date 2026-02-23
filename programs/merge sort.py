#Merge sort

n = int(input("Enter value of n: "))
arr = []
for i in range(n):
    arr.append(int(input()))

print("Original array is: ", arr)

def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def divide(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    divide(arr, low, mid)
    divide(arr, mid + 1, high)
    merge(arr, low, mid, high)

# CALL merge sort
divide(arr, 0, n - 1)
print("Sorted array is:", arr)

'''
Output:
Enter value of n: 4
8
1
29
0
Original array is: [8, 1, 29, 0]
Sorted array is: [0, 1, 8, 29]
'''
