'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to count number of subtrees having sum equal to given sum.
def countSubtreesWithSumX(root, x):
    c = 0
    def rec(root):
        nonlocal c
        if not root:
            return 0
        left = rec(root.left)
        right = rec(root.right)
        s = left+root.data+right
        if s == x:
            c += 1
        return s
    rec(root)
    return c