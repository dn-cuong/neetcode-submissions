class Solution:
    def __init__(self):
        self.max_diameter = 0  

    def helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_height = self.helper(node.left)
        right_height = self.helper(node.right)
        
        self.max_diameter = max(self.max_diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_diameter
