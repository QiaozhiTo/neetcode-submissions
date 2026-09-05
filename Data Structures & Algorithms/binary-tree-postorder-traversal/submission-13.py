# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def dfs(node):
#             if not node:return 
#             dfs(node.left)
#             dfs(node.right)
#             res.append(node.val)
#         dfs(root)
#         return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = [False]
        stack = [root]
        res = []
        while stack:
            v, node = visit.pop(), stack.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    stack.append(node)
                    visit.append(True)
                    stack.append(node.right)
                    visit.append(False)
                    stack.append(node.left)
                    visit.append(False)
        return res