# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        Diameter = left + right
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(Diameter, sub)


    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         res = 0

#         def dfs(root):
#             nonlocal res
#             if not root: return 0
#             left = dfs(root.left)
#             right = dfs(root.right)
#             diameter = left + right
#             res = max(res, diameter)
#             return 1 + max(left, right)

#         dfs(root)
#         return res
