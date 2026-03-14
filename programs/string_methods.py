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

g = "        -hello-          "
print(g.strip())

'''Output:
-hello-
'''

# lstrip()
# Definition:
# Removes spaces from the left side of a string.

h = "   hello"
print(h.lstrip())

'''Output:
hello
'''

# rstrip()
# Definition:
# Removes spaces from the right side of a string.

i = "world   "
print(i.rstrip())

'''Output:
world
'''

# replace()
# Definition:
# Replaces a substring with another substring.

# Use:
# Modify or clean text.

j = "I like Java"
print(j.replace("Java", "Python"))

'''Output:
I like Python
'''

# split()
# Definition:
# Splits a string into a list.

# Use:
# Breaking text into words.

k = "apple banana mango"
print(k.split())

'''Output:
['apple', 'banana', 'mango']
'''

# join()
# Definition:
# Joins elements of a list into a string.

# Use:
# Combining words.

words = ["Python", "is", "fun"]
print(" ".join(words))

'''Output:
Python is fun
'''

# find()
# Definition:
# Returns the index of the first occurrence of a substring.

# Use:
# Searching text.

l = "hello world"
print(l.find("world"))

'''Output:
6'''

# index()
# Definition:
# Same as find() but raises an error if substring is not found.

m = "hello"
print(m.index("e"))

'''Output:
1
'''

# startswith()
# Definition:
# Checks if a string starts with a given value.

n = "python"
print(n.startswith("py"))

'''Output:
True
'''


# endswith()
# Definition: Checks if string ends with given suffix.

c = "Hello , how are you"
print(c.endswith("ou"))
'''
Output: True
'''

# isalpha()
# Definition:
# Returns True if all characters are alphabets.

o = "hello"
print(o.isalpha())

'''Output:
True
'''

# isdigit()
# Definition:
# Returns True if all characters are digits.

p = "12345"
print(p.isdigit())

'''Output:
True
'''

# isalnum()
# Definition:
# Returns True if string contains only letters and numbers.

q = "abc123"
print(q.isalnum())

'''Output:
True
'''

# isspace()
# Definition:
# Returns True if string contains only whitespace.

r = "   "
print(r.isspace())

'''Output:
True
'''

# swapcase()
# Definition:
# Converts lowercase letters to uppercase and vice versa.

t = "HELLO world"
print(t.swapcase())

'''Output:
hello WORLD
'''

