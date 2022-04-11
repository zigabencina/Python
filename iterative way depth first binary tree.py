class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values(root):
    if root == None:
        return []
    stack = [ root ]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.val)


        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        

    return result

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