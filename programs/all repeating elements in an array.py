#Printing all the repeating elements in an array
n = int(input("Enter  the size of array: "))
arr =[]
for i in range(n):
    arr.append(int(input(f"Enter the element for index {i}: ")))

print(arr)

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
    
for key, values in freq.items():
    if values > 1:
        print(key, end = " ")

'''Output:
Enter  the size of array: 8
Enter the element for index 0: 1
Enter the element for index 1: 1
Enter the element for index 2: 2
Enter the element for index 3: 8
Enter the element for index 4: 5
Enter the element for index 5: 5
Enter the element for index 6: 8
Enter the element for index 7: 5
[1, 1, 2, 8, 5, 5, 8, 5]
1 8 5
'''
