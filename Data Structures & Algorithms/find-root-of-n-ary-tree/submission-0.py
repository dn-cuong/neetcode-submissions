class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()

        for node in tree:
            for child in node.children:
                children.add(child)

        for node in tree:
            if node not in children:
                return node