#capitalize()
# Definition: Converts the first character to uppercase and rest to lowercase.
# Use: Formatting sentences.

s = "python PROGRAMming"
print(s.capitalize())

'''Output:
Python programming
'''



#casefold()
#Definition: Converts string to lowercase for case-insensitive comparison.

#Use: Useful for comparing strings regardless of case.


a = "HELLOOO"
print(a.casefold())

'''
Output:
hellooo
'''


# count(substring)
# Definition: Counts occurrences of a substring.
 
b = "banana and apple"
print(b.count("a"))

''' Output: 5
'''


# endswith()
# Definition: Checks if string ends with given suffix.

c = "Hello , how are you"
print(c.endswith("ou"))
'''
Output: True
'''

# upper()
# Definition:
# Converts all characters of a string to uppercase.

# Use:
# Used when you want text in capital letter

d = "hello world"
print(d.upper())

'''
Output:
HELLO WORLD
'''

# lower()
# Definition:
# Converts all characters of a string to lowercase.

# Use:
# Used to normalize text for comparison.

e = "HELLO"
print(e.lower())

'''Output:
hello
'''

# title()
# Definition:
# Converts the first letter of every word to uppercase.

# Use:
# Used for headings or titles.

f = "python programming language"
print(f.title())

'''Output
Python Programming Language
'''


# strip()
# Definition:
# Removes spaces from the beginning and end of a string.

# Use:
# Cleaning user input.

s = "        -hello-          "
print(s.strip())

'''Output:
-hello-
'''