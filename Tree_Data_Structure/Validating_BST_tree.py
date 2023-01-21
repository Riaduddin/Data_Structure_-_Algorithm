class Solution:
    def isValidBST(self, root) -> bool:
        if root is None or root.left is None or root.right is None:
            return root
        elif root.val==root.left.val and root.val==root.right.val:
            return False
        elif root.right.val>root.left.val and root.val <root.right.val and root.val> root.left.val:
            return Solution().isValidBST(root.right)
            return Solution().isValidBST(root.left)
        else:
            return False