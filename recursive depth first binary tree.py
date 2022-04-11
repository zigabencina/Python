
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values(root):
    if root == None:
        return []
    left_values = depth_first_values(root.left) # [ b ,d ,e ]
    right_values = depth_first_values(root.right)  # [ c, f ]
    return [ root.val, *left_values, *right_values ]




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
c.left = g



print(depth_first_values(a))