#  Linear search

n = int(input("Enter value of n: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("array is", arr)
key = int(input("Enter element to search: "))
for i in range(n):
    if arr[i] == key:
        print("Element", key," is found at index", i)
    else:
        print("Element is not present in array")

'''
Output:
Enter value of n: 5
6
5
4
7
2
array is [6, 5, 4, 7, 2]
Enter element to search: 5
Element 5  is found at index 1
'''
