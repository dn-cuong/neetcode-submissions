"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return []
        def dfs(root):
            if not root:
                return None
            for i in range(len(root.children)):
                dfs(root.children[i])
                ans.append(root.children[i].val)


        dfs(root)

        return ans + [root.val]