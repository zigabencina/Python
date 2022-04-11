
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





a = Node(5)
b = Node(6)
c = Node(-1)
d = Node(12)
e = Node(3)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f




print(depth_first_values(a))
sum_arr = 0
list = depth_first_values(a)


for i in depth_first_values(a):
        
    sum_arr += i

print(sum_arr)


