#capitalize()
# Definition: Converts the first character to uppercase.
# Use: Formatting sentences.

s = "python programming"
print(s.capitalize())

'''Output:
Python programming
'''


'''
casefold()
Definition: Converts string to lowercase for case-insensitive comparison.

Use: Useful for comparing strings regardless of case.
'''

a = "HELLOOO"
print(a.casefold())

'''
Output:
hellooo
'''

'''
count(substring)
Definition: Counts occurrences of a substring.
'''
b = "banana and apple"
print(b.count("a"))

'''Output: 5
'''


# endswith()
# Definition: Checks if string ends with given suffix.

c = "Hello , how are you"
print(c.endswith("ou"))
# output: True