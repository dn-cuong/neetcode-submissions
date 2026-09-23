class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def checkBST(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (checkBST(node.left, low, node.val) and
                    checkBST(node.right, node.val, high))

        def count(node):
            if not node:
                return 0

            return 1 + count(node.left) + count(node.right)

        def dfs(node):
            if not node:
                return 0

            # DFS left/right
            left = dfs(node.left)
            right = dfs(node.right)

            # Check subtree rooted at current node
            if checkBST(node, float("-inf"), float("inf")):
                return max(left, right, count(node))

            return max(left, right)

        return dfs(root)