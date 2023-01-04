class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def isMirror(left,right):
    if left is None or right is None:
        return True
    if left.val != right.val:
        return False
    return isMirror(left.left,right.right) and isMirror(left.right,right.left)

def isSymmetric(root):
    if root is None:
        return True
    else:
        return isMirror(root.left,root.right)

    

root=Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right.left=Node(4)
root.right.right=Node(3)

if isSymmetric(root) == True:
    print('Symmetric Tree')
else:
    print('Not Symmetric Tree')

# Sample Test Case 2
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(3)
root.right.right = Node(3)
if isSymmetric(root) == True:
    print("Symmetric Tree")
else:
    print("Not Symmetric Tree")