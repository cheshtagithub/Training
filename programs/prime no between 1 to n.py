#Prime no between 1 to n

n = int(input("Enter the no.: "))
print("prime no. between 1 to ",n ,"is")
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i )
        
        '''
Output:
Enter the no.: 87
prime no. between 1 to  87 is
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
'''
