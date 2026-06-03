# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
#         if not root:return None
#         # 把“删除叶子”这件事放在了递归之前检查，导致会漏删“递归后新变成叶子”的节点。
#         if not root.left and not root.right and root.val == target:
#             return None
#         root.left = self.removeLeafNodes(root.left, target)
#         root.right = self.removeLeafNodes(root.right, target)
#         return root
# [3,null,3] output：【3, null, 3]

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root: return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
