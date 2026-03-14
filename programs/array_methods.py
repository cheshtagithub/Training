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
