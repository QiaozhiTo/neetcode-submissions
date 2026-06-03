# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = []
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                res.append(level)
        return len(res)

