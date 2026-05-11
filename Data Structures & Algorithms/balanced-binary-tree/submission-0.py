class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        left_height = height(root.left)
        right_height = height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)