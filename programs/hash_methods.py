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