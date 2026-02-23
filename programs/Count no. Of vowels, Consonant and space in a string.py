 '''           ​ Count no. Of vowels, Consonant and space in a string'''
 
 n = input("Enter the string :")
x = n.lower()
vowels = 0
consonant = 0
space = 0
for i in range(len(n)):
    ch = x[i]
    if ch in "aeiou":
        vowels += 1
    elif ch == " ":
        space += 1
    elif ch.isalpha():
        consonant += 1
print("Total no. of Vowels, consonant and space in string are: ")
print("Vowels:", vowels, "\nConsonant:", consonant, "\nSpace:", space)

'''
Output: 
Enter the string :Hello My name IS 
Total no. of Vowels, consonant and space in string are: 
Vowels: 5 
Consonant: 8 
Space: 4
'''
