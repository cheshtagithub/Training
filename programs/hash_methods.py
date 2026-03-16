# 1. clear()
# Description: Removes all elements from the dictionary.

d = {"name": "John", "age": 25}
d.clear()
print(d)

'''Output:
{}
'''

# 2. copy()
# Description: Returns a shallow copy of the dictionary.

d = {"name": "John", "age": 25}
new_d = d.copy()
print(new_d)

'''Output:
{'name': 'John', 'age': 25}
'''

# 3. fromkeys()
# Description: Creates a dictionary with given keys and a common value.

keys = ("a", "b", "c")
d = dict.fromkeys(keys, 33)
print(d)

'''Output:
{'a': 33, 'b': 33, 'c': 33}
'''

# 4. get()
# Description: Returns the value of a key. If key is not found, it returns a default value instead of error.

d = {"name": "John", "age": 25}
print(d.get("name"))
print(d.get("city", "Not Found"))

'''Output:
John
Not Found
'''

# 5. items()
# Description: Returns all key-value pairs as tuples.

d = {"name": "John", "age": 25}
print(d.items())

'''Output:
dict_items([('name', 'John'), ('age', 25)])
'''

# 6. keys()
# Description: Returns all keys from the dictionary.

d = {"name": "John", "age": 25}
print(d.keys())

'''Output:
dict_keys(['name', 'age'])
'''

# 7. values()
# Description: Returns all values from the dictionary.

d = {"name": "John", "age": 25}
print(d.values())

'''Output:
dict_values(['John', 25])
'''

# 8. pop()
# Description: Removes the element with the specified key and returns its value.

d = {"name": "John", "age": 25}
x = d.pop("age")
print(x)
print(d)

'''Output:
25
{'name': 'John'}
'''

# 9. popitem()
# Description: Removes and returns the last inserted key-value pair.

d = {"name": "John", "age": 25}
x = d.popitem()
print(x)
print(d)

'''Output:
('age', 25)
{'name': 'John'}
'''

# 10. setdefault()
# Description: Returns the value of a key. If the key does not exist, it inserts the key with a specified value.

d = {"name": "John"}
d.setdefault("age", 25)
print(d)

'''Output:
{'name': 'John', 'age': 25}
'''

# 11. update()
# Description: Updates the dictionary with another dictionary or key-value pairs.

d = {"name": "John"}
d.update({"age": 25})
print(d)

'''Output:
{'name': 'John', 'age': 25}
'''