# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []
#         res = []
#         curr = root
#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left  
#             curr = stack.pop()
#             res.append(curr.val)
#             curr = curr.right
#         return res[k-1]

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(node):
            if not node: return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res[k-1]
                   