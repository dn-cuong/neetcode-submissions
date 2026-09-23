"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        def dfs(curr):
            if not curr:
                return
            
            for child in curr.children:
                dfs(child)
            res.append(curr.val)
        
        dfs(root)
        return res