# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):

        #by me
        dummy=root
        left=root.left if root else None
        right=root.right if root else None
        # while left and right:
        if root:
            root.left=right
            root.right=left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return dummy



        #By Neetcode
        # if not root:
        #     return None
        
        # tmp=root.left
        # root.left=root.right
        # root.right=tmp

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root