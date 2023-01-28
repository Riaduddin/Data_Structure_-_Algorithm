class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        max_value=[root.val]
        def dfs(root):
            if not root:
                return 0
            leftmax=dfs(root.left)
            print('leftmax',leftmax)
            rightmax=dfs(root.right)
            print('rightmax',rightmax)
            leftmax=max(leftmax,0)
            rightmax=max(rightmax,0)

            max_value[0]=max(max_value[0],root.val+leftmax+rightmax)

            return root.val+max(leftmax,rightmax)
        
        dfs(root)
        return max_value[0]