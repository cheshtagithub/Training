#Quick sort

n = int(input("Enter value of n: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("Original array is:", arr)
def partition(arr, low, high):
    pivot = arr[high]   
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
quickSort(arr, 0, n - 1)
print("Sorted array is:", arr)

'''
Output:
Enter value of n: 5
90
8
2
99
0
Original array is: [90, 8, 2, 99, 0]
Sorted array is: [0, 2, 8, 90, 99]
'''
