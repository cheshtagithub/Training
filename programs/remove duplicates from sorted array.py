#Removing duplicates from sorted array
n = int(input("Enter  the size of array: "))
arr =[]
for i in range(n):
    arr.append(int(input(f"Enter the element for index {i}: ")))

print(arr)

i = 0

for j in range(1, n):
    if arr[i] != arr[j]:
        i += 1
        arr[i] = arr[j]
        
print(arr[:i+1])

'''Output:
Enter  the size of array: 9
Enter the element for index 0: 1
Enter the element for index 1: 1
Enter the element for index 2: 2
Enter the element for index 3: 2
Enter the element for index 4: 3
Enter the element for index 5: 3
Enter the element for index 6: 3
Enter the element for index 7: 3
Enter the element for index 8: 3
[1, 1, 2, 2, 3, 3, 3, 3, 3]
[1, 2]
'''
