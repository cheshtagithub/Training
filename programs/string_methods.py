#1. capitalize()
# Definition: Converts the first character to uppercase and rest to lowercase.
# Use: Formatting sentences.

s = "python PROGRAMming"
print("capitalize: ",s.capitalize())

'''Output:
Python programming
'''



#2. casefold()
#Definition: Converts string to lowercase for case-insensitive comparison.

#Use: Useful for comparing strings regardless of case.


a = "HELLOOO"
print("casefold: ",a.casefold())

'''
Output:
hellooo
'''


#3. count(substring)
# Definition: Counts occurrences of a substring.
 
b = "banana and apple"
print("count: ",b.count("a"))

''' Output: 5
'''


#4. upper()
# Definition:
# Converts all characters of a string to uppercase.

# Use:
# Used when you want text in capital letter

d = "hello world"
print("upper: ",d.upper())

'''
Output:
HELLO WORLD
'''

#5. lower()
# Definition:
# Converts all characters of a string to lowercase.

# Use:
# Used to normalize text for comparison.

e = "HELLO"
print("lower: ",e.lower())

'''Output:
hello
'''

#6. title()
# Definition:
# Converts the first letter of every word to uppercase.

# Use:
# Used for headings or titles.

f = "python programming language"
print("title: ",f.title())

'''Output
Python Programming Language
'''


#7. strip()
# Definition:
# Removes spaces from the beginning and end of a string.

# Use:
# Cleaning user input.

g = "        -hello-          "
print("strip: ",g.strip())

'''Output:
-hello-
'''

#8. lstrip()
# Definition:
# Removes spaces from the left side of a string.

h = "   hello"
print("lstrip: ",h.lstrip())

'''Output:
hello
'''

#9. rstrip()
# Definition:
# Removes spaces from the right side of a string.

i = "world   "
print("rstrip: ",i.rstrip())

'''Output:
world
'''

#10. replace()
# Definition:
# Replaces a substring with another substring.

# Use:
# Modify or clean text.

j = "I like Java"
print("replace: ",j.replace("Java", "Python"))

'''Output:
I like Python
'''

#11. split()
# Definition:
# Splits a string into a list.

# Use:
# Breaking text into words.

k = "apple banana mango"
print("split: ",k.split())

'''Output:
['apple', 'banana', 'mango']
'''

#12. join()
# Definition:
# Joins elements of a list into a string.

# Use:
# Combining words.

words = ["Python", "is", "fun"]
print("join: "," ".join(words))

'''Output:
Python is fun
'''

#13. find()
# Definition:
# Returns the index of the first occurrence of a substring.

# Use:
# Searching text.

l = "hello world"
print("find: ",l.find("world"))

'''Output:
6'''

#14. index()
# Definition:
# Same as find() but raises an error if substring is not found.

m = "hello"
print("index: ",m.index("e"))

'''Output:
1
'''

#15. startswith()
# Definition:
# Checks if a string starts with a given value.

n = "python"
print("startswith: ",n.startswith("py"))

'''Output:
True
'''


#16. endswith()
# Definition: Checks if string ends with given suffix.

c = "Hello , how are you"
print("endswith: ",c.endswith("ou"))
'''
Output: True
'''

#17. isalpha()
# Definition:
# Returns True if all characters are alphabets.

o = "hello"
print("isalpha: ",o.isalpha())

'''Output:
True
'''

#18. isdigit()
# Definition:
# Returns True if all characters are digits.

p = "12345"
print("isdigit: ",p.isdigit())

'''Output:
True
'''

#19. isalnum()
# Definition:
# Returns True if string contains only letters and numbers.

q = "abc123"
print("isalnum: ",q.isalnum())

'''Output:
True
'''

#20. isspace()
# Definition:
# Returns True if string contains only whitespace.

r = "   "
print("isspace: ",r.isspace())

'''Output:
True
'''

#21. swapcase()
# Definition:
# Converts lowercase letters to uppercase and vice versa.

t = "HELLO world"
print("swapcase: ",t.swapcase())

'''Output:
hello WORLD
'''

#22. center()
# Definition:
# Centers the string within a specified width.

u = "Python"
print("center: ",u.center(20, "-"))

'''Output:
-------Python-------
'''

#23. zfill()
# Definition:
# Adds zeros at the beginning of a string.

v = "42"
#23. zfill()
print("zfill: ",v.zfill(5))

'''Output:
00042
'''

#24. format()
# Definition:
# Formats values into a string.

name = "Cheshta"
print("format: ","Hello {}".format(name))

'''Output:
Hello Cheshta
'''

#25. partition()
# Definition: Splits string into three parts.

w = "hello-world"
print("partition: ",w.partition("-"))

'''Output:
('hello', '-', 'world')
'''

#26. rfind()
# Definition: Finds last occurrence of the word or letter.
x = "banana and chocolate"
print("rfind: ",x.rfind("a"))

'''Output:
17
'''

# 27. encode()
# Definition: Converts string into bytes.

s = "hello"
print("encode: ",s.encode())

'''Output:
b'hello'
'''

# 28. expandtabs()
# Definition: Replaces tab \t with spaces.

s = "Hello\tWorld"
print("expandtabs: ",s.expandtabs(4))

'''Output:
Hello   World
'''

# 29.format_map()
# Definition: Formats string using dictionary.

data = {"name": "John"}
print("format_map: ","My name is {name}".format_map(data))

'''Output:
My name is John
'''

# 30. isascii()
# Definition: Checks if characters are ASCII.

s = "hello"
print("isascii: ",s.isascii())

'''Output:
True
'''

# 31. isdecimal()
# Definition: Checks if all characters are decimal numbers.

s = "123"
print("isdecimal: ",s.isdecimal())

'''Output:
True
'''

# 32. isidentifier()
# Definition: Checks if string is valid Python identifier.

s = "variable1"
print("isidentifier: ",s.isidentifier())

'''Output:
True
'''

# 33. islower()
# Definition: Checks if all letters are lowercase.

s = "hello"
print("islower: ",s.islower())

'''Output:
True
'''

# 34. isnumeric()
# Definition: Checks if string contains numeric characters.

s = "123"
print("isnumeric: ",s.isnumeric())

'''Output:
True
'''

# 35. isprintable()
# Definition: Checks if characters are printable.

s = "hello"
print("isprintable: ",s.isprintable())

'''Output:
True
'''

# 36. istitle()
# Definition: Checks if string is in title case.

s = "Hello World"
print("istitle: ",s.istitle())

'''Output:
True
'''

# 37. isupper()
# Definition: Checks if letters are uppercase.

s = "HELLO"
print("isupper: ",s.isupper())

'''Output:
True
'''

# 38. ljust()
# Definition: Left aligns string.

s = "hello"
print("ljust: ",s.ljust(10))

'''Output:
'hello     '
'''

# 39. maketrans()
# Definition: Creates translation table.

table = str.maketrans("a","b")
print("maketrans: ","apple".translate(table))

'''Output: 
bpple
'''

40. 
41. 
42. 
43. 
44. 
45. 
46. 
47. 