# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        diameter = leftDepth + rightDepth
        subMax = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(subMax, diameter)

        

    def maxDepth(self,root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        