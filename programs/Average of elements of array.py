#average of an array
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))
total = 0
for i in range(n):
    total = total + arr[i]

avg = total / n
print("Average of elements of array is: ",avg)

'''Output:
Enter size of array: 5
Enter data for index 0: 1
Enter data for index 1: 2
Enter data for index 2: 3
Enter data for index 3: 4
Enter data for index 4: 5
Average of elements of array is:  3.0
'''
