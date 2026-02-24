#left rotating the elements of array by k elements
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))
d = int(input("Enter the numer of elements to rotate in array: "))   
print(arr)
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
def left_rotate(arr, d):
    n = len(arr)
    
    d = d % n
    if d == 0 or d == n:
        return
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n-1)
left_rotate(arr, d)   
print(arr)

'''Output:
Enter size of array: 5
Enter data for index 0: 8
Enter data for index 1: 7
Enter data for index 2: 6
Enter data for index 3: 5
Enter data for index 4: 4
Enter the numer of elements to rotate in array: 2
[8, 7, 6, 5, 4]
[6, 5, 4, 8, 7]
'''
