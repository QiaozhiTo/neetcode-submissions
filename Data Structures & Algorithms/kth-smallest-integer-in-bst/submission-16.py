# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         res = []
#         def dfs(node):
#             # res = []
#             if not node: return 
#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)
#         dfs(root)
#         return res[k-1]

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         res, stack = [], []
#         cur = root
#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right
#         return res[k-1]

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

