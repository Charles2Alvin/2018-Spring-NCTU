class WriteFile(object):
	"""docstring for WriteFile"""
	def __init__(self):
		super(WriteFile, self).__init__()
		self.file = ''	
RED = "red"
BLACK = "black"
class RB_Tree_Node(object):
	def __init__(self, x):
		self.key = x
		self.left = None
		self.right = None
		self.p = None
		self.color = BLACK
class RB_Tree(object):
	def __init__(self):
		self.nil = RB_Tree_Node(0)
		self.root = self.nil
def LEFT_ROTATE(T,x):
	y = x.right
	x.right = y.left#turn y's left subtree to x's right subtree
	if y.left != T.nil:
		y.left.p = x#if y's left subtree exists,link it to x
	y.p = x.p#set y's parent as x's
	if x.p == T.nil:
		T.root = y#y becomes the root if x was the root
	elif x.p.left == x:
		x.p.left = y
	else: 
		x.p.right = y
	y.left = x
	x.p = y#y becomes x's parent
def RIGHT_ROTATE(T,x):
	y = x.left
	x.left = y.right#turn y's right subtree to x's left subtree
	if y.right != T.nil:
		y.right.p = x#if y's left subtree exists,link it to x
	y.p = x.p#set y's parent as x's
	if x.p == T.nil:
		T.root = y#y becomes the root if x was the root
	elif x.p.right == x:
		x.p.right = y
	else: 
		x.p.left = y
	y.right = x
	x.p = y#y becomes x's parent
def RB_INSERT(T,z):#insert node z to tree T
	y = T.nil
	x = T.root
	while x != T.nil:#find a position to insert
		y = x#y is the node to insert
		if z.key < x.key:
			x = x.left
		else: x = x.right
	z.p = y
	if y == T.nil:#means empty tree
		T.root = z
	elif z.key < y.key:
		y.left = z
	else: y.right = z
	z.left = T.nil
	z.right = T.nil
	z.color = RED#if black, it violates black height
	RB_INSERT_FIXUP(T,z)
def RB_INSERT_FIXUP(T,z):
	while z.p.color == RED:#z and z's parent being red violates property 4
		if z.p == z.p.p.left:
			y = z.p.p.right#y is z's uncle
			if y.color == RED:#Case 1:uncle is red
				z.p.color = BLACK
				y.color = BLACK
				z.p.p.color = RED
				z = z.p.p#向上迭代
			else: 
				if z == z.p.right:#Case 2: uncle is black and z is right child
					z = z.p
					LEFT_ROTATE(T,z)
				z.p.color = BLACK#Case 3:uncle is black and z is left child
				z.p.p.color = RED
				RIGHT_ROTATE(T,z.p.p)
		else:
			y = z.p.p.left#y is z's uncle
			if y.color == RED:#Case 1:uncle is red
				z.p.color = BLACK
				y.color = BLACK
				z.p.p.color = RED
				z = z.p.p#向上迭代
			else: 
				if z == z.p.left:#Case 2: uncle is black and z is right child
					z = z.p
					RIGHT_ROTATE(T,z)
				z.p.color = BLACK#Case 3:uncle is black and z is left child
				z.p.p.color = RED
				LEFT_ROTATE(T,z.p.p)
	T.root.color = BLACK#apply when insert into empty tree
def RB_DELETE(T,z):
	#print(z.left.key)
	y = z#set y as z if z has single children,remove y directly
	y_original_color = y.color#x represents the node moved to y's position
	if z.left == T.nil:#maintain y as the node either removed from or within the tree
		x = z.right
		RB_TRANSPLANT(T,z,z.right)
	elif z.right == T.nil:
		x = z.left
		RB_TRANSPLANT(T,z,z.left)
	else: 
		y = TREE_MINIMUM(T,z.right)
		y_original_color = y.color
		x = y.right
		#print('x.p.key	',x.p.key)
		if y.p == z:#means z's successor is z's right child
			x.p = y#y replaces z and x.p should not be z
		else: 
			RB_TRANSPLANT(T,y,y.right)
			#print('x.p.key	',x.p.key)
			y.right = z.right
			y.right.p = y
		RB_TRANSPLANT(T,z,y)#key step,replace z with z's right's minimum
		y.left = z.left
		y.left.p = y
		y.color = z.color
	if y_original_color == BLACK:#if black,it violates property 4
		RB_DELETE_FIXUP(T,x)	
def RB_DELETE_FIXUP(T,x):
	while x != T.root and x.color == BLACK:
		#print('delete fix up    x de key:',x.key)
		#print('delete fix up	x.p.key:',x.p.key)
		if x == x.p.left:
			w = x.p.right  #maintain w as x's sibling
			if w.color == RED: 			#Case 1		uncle w is red
				w.color = BLACK 		#Case 1
				x.p.color = RED 		#Case 1
				LEFT_ROTATE(T,x.p) 		#Case 1
				w = x.p.right 			#Case 1
			if w.right.color == BLACK and w.left.color == BLACK:
				w.color = RED			#Case 2		uncle is black and both its children are black
				x = x.p					#Case 2
			else:
				if w.right.color == BLACK:		#Case 3		uncle is black and has red left child 
					w.left.color = BLACK		#Case 3		and black right child
					w.color = RED				#Case 3
					RIGHT_ROTATE(T,w)			#Case 3
					w = x.p.right				#Case 3
				w.color = x.p.color 			#Case 4		uncle is black its right child is red
				w.right.color = BLACK			#Case 4
				x.p.color = BLACK
				LEFT_ROTATE(T,x.p)				#Case 4
				x = T.root						#Case 4
		else:
			w = x.p.left
			if w.color == RED:
				w.color = BLACK
				x.p.color = RED
				RIGHT_ROTATE(T,x.p)
				w = x.p.left
			if w.left.color == BLACK and w.right.color == BLACK:
				w.color = RED
				x = x.p
			else:
				if w.left.color == BLACK:
					w.right.color = BLACK
					w.color = RED
					LEFT_ROTATE(T,w)
					w = x.p.left
				w.color = x.p.color
				w.left.color = BLACK
				x.p.color = BLACK
				RIGHT_ROTATE(T,x.p)
				x = T.root
	x.color = BLACK
def RB_TRANSPLANT(T,u,v):
	if u.p == T.nil:#parent being nil means u is the root
		T.root = v
	elif u == u.p.left:
		u.p.left = v
	else: 
		u.p.right = v
	v.p = u.p#let v be u.p's child
	#print('transplant',v.p.key)
def TREE_MINIMUM(T,x):
	while x.left != T.nil:
		x = x.left
	return x
	#border
	
def INORDER_TREEWALK(x,result):
	if x!= None:
		INORDER_TREEWALK(x.left,result)
		if x.key!=0:
			if x.p.key == 0:
				#print('key: ', x.key,'color: ',x.color,' parent: ',x.p.key)
				result.file += 'key: '+str(x.key)+' parent: '+' '+' color: '+str(x.color)+'\n'
			else:
				#print('key: ', x.key,'color: ',x.color,' parent: ',x.p.key)
				result.file += 'key: '+str(x.key)+' parent: '+str(x.p.key)+' color: '+str(x.color)+'\n'
		INORDER_TREEWALK(x.right,result)
def TREE_SEARCH(T,x):
	while T != None and T.key != x:
		if x < T.key:
			T = T.left
		else: T = T.right
	return T
def Run():
	result = WriteFile()#store the data to be wirtten in file
	result.file = ''
	set_fun = 0#record if the function has been set
	fun = 0#record the function option
	NumOfWork = 0#record how many work is to be done
	T = RB_Tree()
	file = 'input.txt'
	with open(file) as f:
		for line in f:
			a = line.split()
			if NumOfWork == 0:
				NumOfWork = a[0]
				continue
			else:
				if fun == 0:
					fun = a[0]
					continue
				else:
					if fun == '1':#insert
						result.file += 'Insert: '
						for node in a:
							result.file += str(node)
							if node != a[-1]:
								result.file += ', '
						result.file += '\n'

						for node in a:
							RB_INSERT(T,RB_Tree_Node(int(node)))
						INORDER_TREEWALK(T.root,result)
						fun = 0 
						set_fun = 0
						continue

					elif fun == '2':#delete

						result.file += 'Delete: '
						for node in a:
							result.file += str(node)
							if node != a[-1]:
								result.file += ', '
						result.file += '\n'
						
						for node in a:
							t = TREE_SEARCH(T.root,int(node))
							if t == None:
								print('The node u want to delete does not exist')
							else:
								RB_DELETE(T,t)
						INORDER_TREEWALK(T.root,result)
						
						fun = 0
						set_fun = 0
						continue

		outFile = 'output.txt'
		f = open(outFile,'w')
		f.write(result.file)#将结果统一写入文件
		f.close
Run()