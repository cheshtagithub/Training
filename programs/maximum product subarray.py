# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i}: "))
    arr.append(num)

print("Input array:", arr)

pre = 1
suff = 1
ans = float('-inf')

for i in range(n):
    if pre == 0:
        pre = 1
    if suff == 0:
        suff = 1

    pre *= arr[i]
    suff *= arr[n - i - 1]

    ans = max(ans, pre, suff)

print("Maximum Product Subarray:", ans)

'''Output:
Enter size of array: 6
Enter element 0: 1
Enter element 1: 7
Enter element 2: -4
Enter element 3: 3
Enter element 4: 9
Enter element 5: 10
Input array: [1, 7, -4, 3, 9, 10]
Maximum Product Subarray: 270
'''
