# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, mVal):
            nonlocal ans
            if not root:
                return

            if root.val >= mVal:
                ans += 1
                mVal = root.val
            
            dfs(root.left, mVal)
            dfs(root.right, mVal)

        dfs(root, float('-inf'))

        return ans