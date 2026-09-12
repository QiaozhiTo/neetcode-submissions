# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sumPath):
            if not node: return False
            sumPath += node.val
            if not node.left and not node.right:
                return sumPath == targetSum
            return dfs(node.left, sumPath) or dfs(node.right, sumPath)
        return dfs(root, 0)