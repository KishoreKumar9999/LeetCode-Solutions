# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def recur(root, greatest):
            if not root:
                return 0
            res = 1 if root.val>=greatest else 0
            greatest = max(root.val, greatest)
            res+=recur(root.left, greatest)
            res+=recur(root.right, greatest)
            return res
        return recur(root, root.val)

