# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = float('inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return 

            diff1 = abs(node.val - target)
            diff2 = abs(ans - target)

            if diff1 == diff2:
                ans = min(ans, node.val)
            elif diff1 < diff2:
                ans = node.val

            dfs(node.left)
            dfs(node.right)


        dfs(root)

        return ans
            