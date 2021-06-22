"""
red-black properties:
P1.Every node is either red or black.
P2.The root is black.
P3.Every leaf is black.
P4.If a node is red,then both its children are black.
P5.For each node,all simple paths from the node to descendant leaves 
contain the same number of black nodes.
"""
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
	"""docstring for RB-tree"""
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
		else: 
			x = x.right
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
	#print('delete procedure')
	#print('delete:'+str(z.key))
	#print(z.left.key)
	y = z#set y as z if z has single children,remove y directly
	y_original_color = y.color#x represents the node to y's position
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
#Tree-walking
def PREORDER_TREE_WALK(T):
	if T != T.nil:
		print(T.key)
		PREORDER_TREE_WALK(T.left)
		PREORDER_TREE_WALK(T.right)
def INORDER_TREE_WALK(T):
	if T != None:
		INORDER_TREE_WALK(T.left)
		if T.key != 0:
			print('key:',T.key,' parent:',T.p.key,' color:',T.color,' left:',T.left.key,' right',T.right.key)
		INORDER_TREE_WALK(T.right)
def POSTORDER_TREE_WALK(T):
	if T != T.nil:
		POST_ORDER_WALK(T.left)
		POST_ORDER_WALK(T.right)
		print(T.key)
def LEVELORDER_TREE_WALK(T):
	pass
def TREE_SEARCH(T,x):
	while T != None and T.key != x:
		if x < T.key:
			T = T.left
		else: T = T.right
	return T
def TREE_MINIMUM(T,x):
	while x.left != T.nil:
		x = x.left
	return x

T = RB_Tree()
nodes=[5,11,9,7,6,12,5,4,1]
#dele = [11,5]
for node in nodes:
	print("插入结点"+str(node))
	RB_INSERT(T,RB_Tree_Node(node))

INORDER_TREE_WALK(T.root)
i = len(nodes)-1
print('now delete!')
while i>0:
	RB_DELETE(T,T.root)
	i -= 1
	INORDER_TREE_WALK(T.root)
	print('done once')

