# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack = [root]
#         res = []
#         visit = [False]
#         while stack:
#             v = visit.pop()
#             curr = stack.pop()
#             if curr:
#                 if v:
#                     res.append(curr.val)
#                 else:
#                     stack.append(curr)
#                     visit.append(True)
#                     stack.append(curr.right)
#                     visit.append(False)
#                     stack.append(curr.left)
#                     visit.append(False)
#         return res
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorder(node):
            if not node:return 
            postorder(node.left)                 
            postorder(node.right)                 
            res.append(node.val)
        postorder(root)
        return res
                    