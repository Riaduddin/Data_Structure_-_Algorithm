class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def InsertBST(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data==key:
            return root
        elif root.data > key:
            root.left=InsertBST(root.left,key)
        else:
            root.right=InsertBST(root.right,key)
    return root

def inOrder(root):
    if root:
        #recursive call for subtree
        inOrder(root.left)
        print(str(root.data)+ " ", end=' ')
        inOrder(root.right)
def searchBST(root,searchData):
    #Base case condition
    if root is None or root.data==searchData:
        return root
    #left recursive call
    elif root.data>searchData:
        return searchBST(root.left,searchData)

    #right recursive call
    else:
        return searchBST(root.right,searchData)

root=Node(50)
root=InsertBST(root,70)
root=InsertBST(root,80)
root=InsertBST(root,60)
root=InsertBST(root,40)

print("Inorder Traversal")
inOrder(root)

key = 120
result = searchBST(root, key)
print()
if result:
    print("Data is present in BST")
else:
    print("Data is not present in BST")