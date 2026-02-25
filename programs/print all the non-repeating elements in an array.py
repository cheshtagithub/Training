#print all the non-repeating elements in an array.py
n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter the element for index {i}: ")))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Non-repeating elements:", end=" ")
for num in arr:
    if freq[num] == 1:
        print(num, end=" ")

'''Output
Enter the size of array: 9
Enter the element for index 0: 1
Enter the element for index 1: -1
Enter the element for index 2: 1
Enter the element for index 3: 2
Enter the element for index 4: 2
Enter the element for index 5: 3
Enter the element for index 6: 4
Enter the element for index 7: 4
Enter the element for index 8: 4
Non-repeating elements: -1 3
'''
