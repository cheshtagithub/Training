#Reverse of an array

n = [2,5,7,6,8,9]
m = []
x = len(n) - 1
for i in range(x, -1, -1):
    m.append(n[i])
print(m)

'''
Output:
[9, 8, 6, 7, 5, 2]
'''
