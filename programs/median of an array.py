#median of an array
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))

arr.sort()

if n % 2 == 0:
    ind1 = (n // 2) - 1
    ind2 = n // 2
    med = (arr[ind1] + arr[ind2]) / 2
    print("Median is:", med)
    
else:
    print("median is:", arr[n//2])

'''Output:
Enter size of array: 4
Enter data for index 0: 1
Enter data for index 1: 2
Enter data for index 2: 3
Enter data for index 3: 4
Median is: 2.5

Enter size of array: 5
Enter data for index 0: 1
Enter data for index 1: 2
Enter data for index 2: 3
Enter data for index 3: 4
Enter data for index 4: 5
median is: 3

