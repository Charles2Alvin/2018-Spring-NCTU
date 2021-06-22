# m为被除数array1的位长
# n为除数array2的位长
# temp数组存放余数，长度为n
# k从头到尾扫描到array1的元素
array_1 = [1, 1, 0, 1, 0, 0]
array_2 = [1, 0, 1, 0, 1]
temp = [0, 0, 0, 0, 0]
m = len(array_1)
n = len(array_2)
k = n
# 1.构造temp的初值，以后只对temp与array2进行异或
for i in range(n): #i从0变化到n-1
    temp[i] = array_1[i] ^ array_2[i]
print(temp)
flag = 1
print("开始")
while k < m and flag:#令k永远指向往后的一位
    # 2.找到1的最大索引j
    j = 0
    while j<n and temp[j]==0:
        j += 1
    if j >= n:
        break
    print("j="+str(j))
    if j > m-k:
        t = m-k#t表示可补充的位数
        for i in range(n-j):#把后面的元素往前挪，空出t位
            temp[j-t+i] = temp[j+i]
        print("t= "+str(t))
        for i in range(1, t):#向后取t位补齐
            temp[n-i] = array_1[m-i]
        break
    # 3.j恰好是缺少的位数,把后面的元素往前挪，空出j位
    for i in range(n-j):#i从0变化到n-j-1
        temp[i] = temp[j+i]
    #print(temp)
    # 4.向后取j位补齐
    t=j
    i=0
    while t>=1 and i<=j-1:
        temp[n-t] = array_1[k+i]
        t -= 1
        i += 1
    k += j
    print("k= "+str(k))
    if k >= m:
        flag = 0
    print("补齐之后"+str(temp))
    # 5.n位的按位异或
    for i in range(n): #i从0变化到n-1
        temp[i] = temp[i] ^ array_2[i]
    print("异或之后"+str(temp))
print("result "+str(temp))