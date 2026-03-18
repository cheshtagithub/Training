#1. append()
# Definition:
# Adds an element to the end of the list.

# Use:
# Used when you want to add a single item.

arr = [1, 2, 3]
arr.append(4)
print("append: ",arr)

'''Output:
[1, 2, 3, 4]
'''

#2. extend()
# Definition:
# Adds elements from another list to the end.

# Use:
# Used to combine two lists.

arr = [1, 2, 3, 4]
arr.extend([3, 4])
print("extend: ",arr)

'''Output:
[1, 2, 3, 4, 3, 4]
'''

#3. insert()
# Definition:
# Adds an element at a specific index.

# Use:
# Insert element at desired position.

arr = [1, 2, 4, 5, 6, 7]
arr.insert(2, 3)
print("insert: ",arr)

'''Output:
[1, 2, 3, 4, 5, 6, 7]
'''

#4. remove()
# Definition:
# Removes the first occurrence of a value.

# Use:
# Delete a specific value.

arr = [1, 2, 2, 3, 2]
arr.remove(2)
print("remove: ",arr)

'''Output:
[1, 2, 3, 2]
'''

#5. pop()
# Definition:
# Removes element at a given index and returns it.

# Use:
# Useful for stack operations.

arr = [1, 2, 3]
arr.pop()
print("pop: ",arr)

'''Output:
[1, 2]
'''

#6. clear()
# Definition:
# Removes all elements from the list.

arr = [1, 2, 3]
arr.clear()
print("clear: ",arr)

'''Output:
[]
'''

#7. index()
# Definition:
# Returns the index of the first occurrence of a value.

arr = [10, 20, 30]
print("index: ",arr.index(20))

'''Output:
1
'''

#8. count()
# Definition:
# Counts occurrences of a value.

arr = [1, 2, 2, 3, 2, 2, 2, 4]
print("count: ",arr.count(2))

'''Output:
5
'''

#9. sort()
# Definition:
# Sorts the list in ascending order.

arr = [4, 1, 3, 9, 6, 0, 1, 2]
arr.sort()
print("sort: ",arr)

'''Output:
[0, 1, 1, 2, 3, 4, 6, 9]
'''

#10. reverse()
# Definition:
# Reverses the order of elements.

arr = [1, 2, 3, 4, 5, 6, 7]
arr.reverse()
print("reverse: ",arr)

'''Output:
[7, 6, 5, 4, 3, 2, 1]
'''

#11. copy()
# Definition:
# Creates a shallow copy of the list.

arr = [1, 2, 3]
new_arr = arr.copy()
print("copy: ",new_arr)

'''Output:
[1, 2, 3]
'''

#12. len() (built-in but commonly used)
# Definition:
# Returns number of elements in list.

arr = [1, 2, 3, 9, 0, 2, 8]
print("len: ",len(arr))

'''Output:
7
'''


'''
Practice
'''



lst = [4, 2, 7, 2, 9, 4, 1]

# Reverse a array
rev = lst[::-1]
print(rev)

lst.reverse()
print(lst)

'''Output:
[1, 4, 9, 2, 7, 2, 4]
'''

# Find max and min
print("Max:", max(lst))
print("Min:", min(lst))

'''Output:
Max: 9
Min: 1
'''

# Remove duplicates
unique = list(set(lst))
print(unique)


'''Output:
[1, 2, 4, 7, 9]
'''

unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

print(unique)

'''Output:
[4, 2, 7, 9, 1]
'''

# Find second largest number
unique = list(set(lst))
unique.sort(reverse=True)

print("Second largest:", unique[1])

'''Output:
Second largest: 7
'''

# Merge two array
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

merged = lst1 + lst2
print(merged)

'''Output:
[1, 2, 3, 4, 5, 6]
'''

# Count frequency of elements
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)

'''Output:
{4: 2, 2: 2, 7: 1, 9: 1, 1: 1}
'''