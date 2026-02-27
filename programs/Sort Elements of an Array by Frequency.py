#Problem Statement: Given an array of integers, having some duplicate elements, sort the array by frequency .

n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter the element for index {i}: ")))
print(arr)  

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
    
arr.sort(key = lambda x: (-freq[x], x)) 

print(*arr)

'''Output:
Enter the size of array: 8
Enter the element for index 0: 1
Enter the element for index 1: 4
Enter the element for index 2: 1
Enter the element for index 3: 2
Enter the element for index 4: 1
Enter the element for index 5: 3
Enter the element for index 6: 4
Enter the element for index 7: 2
[1, 4, 1, 2, 1, 3, 4, 2]
1 1 1 2 2 4 4 3
'''
