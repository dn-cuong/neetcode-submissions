# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def checkpath(root, targetSum, curr):
            if not root:
                return False
            curr += root.val

            if not root.left and not root.right and curr == targetSum:
                return True
            if checkpath(root.left, targetSum, curr):
                return True
            if checkpath(root.right, targetSum, curr):
                return True

            curr -= root.val

            return False
        return checkpath(root, targetSum, 0)

        
        
        