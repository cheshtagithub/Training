# append()
# Definition:
# Adds an element to the end of the list.

# Use:
# Used when you want to add a single item.

arr = [1, 2, 3]
arr.append(4)
print(arr)

'''Output:
[1, 2, 3, 4]
'''

# extend()
# Definition:
# Adds elements from another list to the end.

# Use:
# Used to combine two lists.

arr = [1, 2, 3, 4]
arr.extend([3, 4])
print(arr)

'''Output:
[1, 2, 3, 4, 3, 4]
'''

# insert()
# Definition:
# Adds an element at a specific index.

# Use:
# Insert element at desired position.

arr = [1, 2, 4, 5, 6, 7]
arr.insert(2, 3)
print(arr)

'''Output:
[1, 2, 3, 4, 5, 6, 7]
'''

# remove()
# Definition:
# Removes the first occurrence of a value.

# Use:
# Delete a specific value.

arr = [1, 2, 2, 3, 2]
arr.remove(2)
print(arr)

'''Output:
[1, 2, 3, 2]
'''

# pop()
# Definition:
# Removes element at a given index and returns it.

# Use:
# Useful for stack operations.

arr = [1, 2, 3]
arr.pop()
print(arr)

'''Output:
[1, 2]
'''

# clear()
# Definition:
# Removes all elements from the list.

arr = [1, 2, 3]
arr.clear()
print(arr)

'''Output:
[]
'''

# index()
# Definition:
# Returns the index of the first occurrence of a value.

arr = [10, 20, 30]
print(arr.index(20))

'''Output:
1
'''

# count()
# Definition:
# Counts occurrences of a value.

arr = [1, 2, 2, 3, 2, 2, 2, 4]
print(arr.count(2))

'''Output:
5
'''

# sort()
# Definition:
# Sorts the list in ascending order.

arr = [4, 1, 3, 9, 6, 0, 1, 2]
arr.sort()
print(arr)

'''Output:
[0, 1, 1, 2, 3, 4, 6, 9]
'''

# reverse()
# Definition:
# Reverses the order of elements.

arr = [1, 2, 3, 4, 5, 6, 7]
arr.reverse()
print(arr)

'''Output:
[7, 6, 5, 4, 3, 2, 1]
'''

# copy()
# Definition:
# Creates a shallow copy of the list.

arr = [1, 2, 3]
new_arr = arr.copy()
print(new_arr)

'''Output:
[1, 2, 3]
'''

# len() (built-in but commonly used)
# Definition:
# Returns number of elements in list.

arr = [1, 2, 3, 9, 0, 2, 8]
print(len(arr))

'''Output:
7
'''