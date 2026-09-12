"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [(root, False)]
        res= []
        if not root: return res
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))
        return res