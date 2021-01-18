class TreeNode:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

	def __repr__(self):
		return repr(self.data)

	def add_left(self, node):
		self.left = node
		if node is not None:
			node.parent = self

	def add_right(self, node):
		self.right = node
		if node is not None:
			node.parent = self

"""
        _10_
       /    \
      5      17
     / \     / \
    3   7   12  19
   / \
  1   4
"""

def create_bst():
	root = TreeNode(10)

	for item in [5,17,3,7,12,19,1,4]:
		node = TreeNode(item)
		root = bst_insert(root,node)
	return root

def in_order(node):
	if node.left:
		in_order(node.left)
	
	print(node,end=" ")

	if node.right:
		in_order(node.right)


def bst_insert(root, node):
	last_node = None
	current_node = root

	while current_node is not None:
		last_node = current_node

		if node.data < current_node.data:
			print(current_node.left)
			current_node = current_node.left
		else:
			print(current_node.right)
			current_node = current_node.right

	if last_node is None:
		root = node
	elif node.data < last_node.data:
		last_node.add_left(node)
	else:
		last_node.add_right(node)

	return root

if __name__ == "__main__":
	root = create_bst()
	print(root.parent)

	print("Root: ", root)

	print("\nIn-order: ",end="")
	in_order(root)