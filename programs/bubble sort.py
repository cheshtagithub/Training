 #    Bubble sort
# to input array by user
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("original array is ", arr)
# bubble sort code
def bubble(arr):
    x = len(arr)
    for i in range(n - 1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]  = arr[j+1], arr[j]
#to print array after sorting
bubble(arr)
print("sorted array is", arr)


"""
Output:
Enter size of array: 4
5
4
7
1
original array is  [5, 4, 7, 1]
sorted array is [1, 4, 5, 7]
"""
