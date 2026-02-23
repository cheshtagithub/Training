#Count frequency of each element in the array

n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))
    
freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
    
for key in freq:
    print(key ,"->", freq[key])
'''Output:
Enter the size of array: 10
Enter data for index 0: 1
Enter data for index 1: 2
Enter data for index 2: 3
Enter data for index 3: 3
Enter data for index 4: 2
Enter data for index 5: 1
Enter data for index 6: 1
Enter data for index 7: 2
Enter data for index 8: 3
Enter data for index 9: 3
1 -> 3
2 -> 3
3 -> 4
'''
