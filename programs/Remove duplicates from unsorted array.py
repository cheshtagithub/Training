#Remove duplicates from unsorted array
n = int(input("Enter  the size of array: "))
arr =[]
for i in range(n):
    arr.append(int(input(f"Enter the element for index {i}: ")))

print(arr)

seen = set()
index = 0
for i in arr:
    if i not in seen:
        seen.add(i)
        arr[index] = i
        index += 1
print(arr[:index])

'''Output:
Enter  the size of array: 9
Enter the element for index 0: 1
Enter the element for index 1: 1
Enter the element for index 2: 1
Enter the element for index 3: 2
Enter the element for index 4: 2
Enter the element for index 5: 3
Enter the element for index 6: 4
Enter the element for index 7: 4
Enter the element for index 8: 5
[1, 1, 1, 2, 2, 3, 4, 4, 5]
[1, 2, 3, 4, 5]
'''
