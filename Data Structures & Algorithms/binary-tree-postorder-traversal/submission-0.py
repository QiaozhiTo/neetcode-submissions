# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack, res = [],[]
        while stack or curr:
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.right
            curr = stack.pop()
            curr = curr.left
        res.reverse()
        return res
        