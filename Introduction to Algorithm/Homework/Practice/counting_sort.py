def COUNTING_SORT(A,B,k):
	C = []
	for i in range(0,k+1):
		C.append(0)
	for j in range(0,len(A)):
		C[A[j]] += 1
	#Now C[i] contains the number of elements equal to i
	for i in range(1,k+1):
		C[i] += C[i-1]
	#Now C[i] contains the number of elements less than or equal to i
	j = len(A)-1
	while j >= 0:
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1
		j -= 1
A = [3,2,6,4,3,8,2,9,1,4]
B = []
for i in range(0,len(A)):
	B.append(0)
COUNTING_SORT(A,B,9)
print(B)