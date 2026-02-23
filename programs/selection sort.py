#Selection sort

n = int(input("Enter size.: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("original array is ",arr)
def selection(arr):
    x = len(arr)
    for i in range(x - 1):
        min_ind = i 
        for j in range(i + 1, x):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]      
selection(arr)
print("sorted array is", arr)

'''
Output:
Enter size.: 5
7
6
5
9
1
original array is  [7, 6, 5, 9, 1]
sorted array is [1, 5, 6, 7, 9]
'''
