def Max_Score(n,p,f,c):
	#k corresonds to course
	for k in range(1,c+1):
		#j corresonds to days
		for j in range(1,n+1):
			for i in range(1,j+1):#i corresponds to days for course k 
				#print("i:"+str(i)+" j:"+str(j)+" k:"+str(k))
				if i > c:
					i = c
				if f[k][j] < int(p[i-1][k-1]) + f[k-1][j-i]:
					f[k][j] = int(p[i-1][k-1]) + f[k-1][j-i]
			for t in range(1,n+1):
				f[k][t] = max(f[k][t],f[k-1][t])
	return f[c][n]
def Run():
	task_begin = 0
	set_course = 0
	set_max_day = 0
	resource = 0
	max_day_for_one = 0
	profit = []
	result = []
	file = 'input.txt'
	with open(file) as f:
		for line in f:
			a = line.split()
			if len(a) == 1:
				resource = int(a[0])
				f = [[0 for j in range(0,resource+1)]for i in range(0,c+1)]
				max = Max_Score(resource,profit,f,c)
				result.append(max)
				task_begin = 1
				continue
			if a != [] and len(a) != 1 and task_begin:
				set_course = 0
				set_max_day = 0
				max_day_for_one = 0
				task_begin = 0
				profit = []
			if a!= [] and len(a) != 1 and task_begin != 1:
				profit.append(a)
			if set_course == 0:
				c = len(a)
				set_course = 1
			if a == []:
				set_max_day = 1
			if set_max_day == 0:
				max_day_for_one += 1
	outFile = 'output.txt'
	f = open(outFile,'w')
	for each in result:
		f.write(str(each)+'\n')
	f.close
	
Run()