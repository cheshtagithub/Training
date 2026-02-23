#Find the second smallest and second largest element in an array

n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter data for index {i}: ")))

def secondSmallest(arr, n):
    
    if n < 2:
        print("There is no second smallest.")
        
    small = float('inf')
    second_small = float('inf')
    
    for i in range(n):
        if small > arr[i]:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and small != arr[i]:
            second_small = arr[i]
            
    return second_small

def secondLargest(arr, n):
    
    if n < 2:
        print("There is no second largest.")
    
    large = float('-inf')
    second_large = float('-inf')
    
    for i in range(n):
        if large < arr[i]:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and large != arr[i]:
            second_large = arr[i]
            
    return second_large
    

print("The second smallest element is: ",secondSmallest(arr, n))

print("The second largest element is: ",secondLargest(arr, n))

'''Output:
Enter the size of array: 5
Enter data for index 0: 9
Enter data for index 1: 8
Enter data for index 2: 7
Enter data for index 3: 6
Enter data for index 4: 5
The second smallest element is:  6
The second largest element is:  8
'''
