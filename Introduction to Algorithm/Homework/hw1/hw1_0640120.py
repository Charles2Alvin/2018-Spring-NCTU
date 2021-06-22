#插入x：x插入到最后一位，将x与左边以及上边的比较，与更大的那个交换，直到两个邻居都比自己小
#删除x：将x赋值为无穷，选择右边和下边的更小者，与之交换，直到两个邻居都比自己大
import sys
x = sys.maxsize
b = []
class table():
	m = 0#row number
	n = 0#column number
	table = []#Young tableau
	leftbound,rightbound,upbound,downbound = [],[],[],[]
	def reset(self):
		self.m = 0
		self.n = 0
		self.table = []
		self.leftbound = []
		self.rightbound = []
		self.upbound = []
		self.downbound = []
	def setBound(self):
		m = self.m
		n = self.n
		size = m*n
		i = 0
		while i<size-1:
			self.leftbound.append(i)
			self.rightbound.append(i+m-1)
			i += m
		i = 0
		while i<m:
			self.upbound.append(i)
			self.downbound.append(i+m*(n-1))
			i += 1
	def insert(self,k):
		#要插入的元素放在末位
		m = self.m
		n = self.n
		table = self.table
		i = m*n-1
		table[i] = k
		#循环直到i超出边界
		while i > 0:
			left = i-1
			up = i-m
			#判断i是否在边界上
			if i in self.leftbound:
				larger = up
			elif i in self.upbound:
				larger = left
			else:
				larger = up
				if table[up] < table[left]:
					larger = left
			#如果需要，则交换位置
			if table[i] < table[larger]:
				temp = table[larger]
				table[larger] = table[i]
				table[i] = temp
				i = larger
			else:
				break
		self.table = table
	def extractMin(self):
		table = self.table
		m = self.m
		n = self.n
		i = 0
		table[i] = x
		while i < m*n:
			right = i+1
			down = i+m
			#选出右下邻居中较小者
			if i in self.rightbound:
				minor = down
			elif i in self.downbound:
				minor = right
			else:
				minor = right
				if table[down] < table[right]:
					minor = down
			#如果需要，则交换位置
			if table[i]>table[minor]:
				temp = table[i]
				table[i] = table[minor]
				table[minor] = temp
				i = minor
			else:
				break
		self.table = table
def Run():
	set_fun = 0
	Num_tab = 0
	set_insert = 0
	result = ''
	insert = []
	ins = table()
	ins.n = 0
	file = 'input.txt'
	with open(file) as f:
		for line in f:
			a = line.split()
			if a == []:
				for i in range(0,len(ins.table)):
					if ins.table[i] == 'x':
						ins.table[i] = sys.maxsize
					ins.table[i] = int(ins.table[i])
				ins.setBound()
				if Fun == '2':
					#检测非法输入
					if ins.table[0] == x:
						print("error:Table empty")
						ins.reset()
						set_fun = 0
						continue
					exm = ins.table[0]
					ins.extractMin()
					#将矩阵写入结果
					count = 0
					result += 'Extract-min '+str(exm)+'\n'
					for i in ins.table:
						if count == ins.m:
							result += '\n'
							count = 0
						if i == sys.maxsize:
							i = 'x'
						i = str(i)
						result += i + ' '
						count += 1
					result += '\n'+'\n'
				elif Fun == '1':
					#检测非法输入
					if ins.table[-1] != x:
						print("error:Table is full")
						ins.reset()
						set_fun = 0
						set_insert = 0
						continue
					count = 0
					insrt = ''
					while insert != []:
						Number = insert[0]
						insert.pop(0)
						insrt += str(int(Number))+' '
						ins.insert(int(Number))
					set_insert = 0
					#加入标题
					result += 'Insert '
					#加入要插入的元素
					for i in insrt:
						result += i
					result += '\n'
					#加入矩阵
					for i in ins.table:
						if count == ins.m:
							result += '\n'
							count = 0
						if i == sys.maxsize:
							i = 'x'
						i = str(i)
						result += i + ' '
						count += 1
					result += '\n'+'\n'
				#功能执行完成之后，进行参数重设
				ins.reset()
				set_fun = 0
				continue
			if Num_tab == 0:
				Num_tab = a[0]
				continue
			if set_fun == 0:
				Fun = a[0]
				set_fun = 1
				continue
			if set_fun == 1:
				if Fun == '1'and set_insert == 0:
					set_insert = 1
					insert = a
					continue
				ins.m = len(a)
				ins.n += 1
				ins.table += a
		outFile = 'output.txt'
		f = open(outFile,'w')
		f.write(str(result))#将结果统一写入文件
		f.close
Run()
