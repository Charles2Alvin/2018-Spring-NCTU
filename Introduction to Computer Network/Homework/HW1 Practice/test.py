"""
a = [1,2,3]
n = len(a)
#print(n)
#print(a[n-1])
for i in range(6,7):
	print(i)
"""

array_1 = [1, 1, 0, 1, 0, 0]
array_2 = [1, 0, 1, 0, 1]
temp = [0, 0, 0, 0, 0]
m = len(array_1)
n = len(array_2)
k = n
for i in range(n):
    temp[i] = array_1[i] ^ array_2[i]
flag = 1
while k < m and flag:
    j = 0
    while j<n and temp[j]==0:
        j += 1
    if j >= n:
        break
    if j > m-k:
        t = m-k
        for i in range(n-j):
            temp[j-t+i] = temp[j+i]
        for i in range(1, t):
            temp[n-i] = array_1[m-i]
        break
    for i in range(n-j):
        temp[i] = temp[j+i]
    t=j
    i=0
    while t>=1 and i<=j-1:
        temp[n-t] = array_1[k+i]
        t -= 1
        i += 1
    k += j
    if k >= m:
        flag = 0
    for i in range(n):
        temp[i] = temp[i] ^ array_2[i]
print("result "+str(temp))