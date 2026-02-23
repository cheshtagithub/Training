#           ​ Frequency of each character of a string 

n = input("Enter the string of number: ")
visited = ""

for ch in n:
    if ch not in visited:
        count = n.count(ch)
        print(ch," : ",count)
        visited += ch

'''
Output:
Enter the string of number: helloolloooloooolooollllloooeheheheheheheeeehhhhhhhhh
h  :  16
e  :  11
l  :  11
o  :  15
'''
