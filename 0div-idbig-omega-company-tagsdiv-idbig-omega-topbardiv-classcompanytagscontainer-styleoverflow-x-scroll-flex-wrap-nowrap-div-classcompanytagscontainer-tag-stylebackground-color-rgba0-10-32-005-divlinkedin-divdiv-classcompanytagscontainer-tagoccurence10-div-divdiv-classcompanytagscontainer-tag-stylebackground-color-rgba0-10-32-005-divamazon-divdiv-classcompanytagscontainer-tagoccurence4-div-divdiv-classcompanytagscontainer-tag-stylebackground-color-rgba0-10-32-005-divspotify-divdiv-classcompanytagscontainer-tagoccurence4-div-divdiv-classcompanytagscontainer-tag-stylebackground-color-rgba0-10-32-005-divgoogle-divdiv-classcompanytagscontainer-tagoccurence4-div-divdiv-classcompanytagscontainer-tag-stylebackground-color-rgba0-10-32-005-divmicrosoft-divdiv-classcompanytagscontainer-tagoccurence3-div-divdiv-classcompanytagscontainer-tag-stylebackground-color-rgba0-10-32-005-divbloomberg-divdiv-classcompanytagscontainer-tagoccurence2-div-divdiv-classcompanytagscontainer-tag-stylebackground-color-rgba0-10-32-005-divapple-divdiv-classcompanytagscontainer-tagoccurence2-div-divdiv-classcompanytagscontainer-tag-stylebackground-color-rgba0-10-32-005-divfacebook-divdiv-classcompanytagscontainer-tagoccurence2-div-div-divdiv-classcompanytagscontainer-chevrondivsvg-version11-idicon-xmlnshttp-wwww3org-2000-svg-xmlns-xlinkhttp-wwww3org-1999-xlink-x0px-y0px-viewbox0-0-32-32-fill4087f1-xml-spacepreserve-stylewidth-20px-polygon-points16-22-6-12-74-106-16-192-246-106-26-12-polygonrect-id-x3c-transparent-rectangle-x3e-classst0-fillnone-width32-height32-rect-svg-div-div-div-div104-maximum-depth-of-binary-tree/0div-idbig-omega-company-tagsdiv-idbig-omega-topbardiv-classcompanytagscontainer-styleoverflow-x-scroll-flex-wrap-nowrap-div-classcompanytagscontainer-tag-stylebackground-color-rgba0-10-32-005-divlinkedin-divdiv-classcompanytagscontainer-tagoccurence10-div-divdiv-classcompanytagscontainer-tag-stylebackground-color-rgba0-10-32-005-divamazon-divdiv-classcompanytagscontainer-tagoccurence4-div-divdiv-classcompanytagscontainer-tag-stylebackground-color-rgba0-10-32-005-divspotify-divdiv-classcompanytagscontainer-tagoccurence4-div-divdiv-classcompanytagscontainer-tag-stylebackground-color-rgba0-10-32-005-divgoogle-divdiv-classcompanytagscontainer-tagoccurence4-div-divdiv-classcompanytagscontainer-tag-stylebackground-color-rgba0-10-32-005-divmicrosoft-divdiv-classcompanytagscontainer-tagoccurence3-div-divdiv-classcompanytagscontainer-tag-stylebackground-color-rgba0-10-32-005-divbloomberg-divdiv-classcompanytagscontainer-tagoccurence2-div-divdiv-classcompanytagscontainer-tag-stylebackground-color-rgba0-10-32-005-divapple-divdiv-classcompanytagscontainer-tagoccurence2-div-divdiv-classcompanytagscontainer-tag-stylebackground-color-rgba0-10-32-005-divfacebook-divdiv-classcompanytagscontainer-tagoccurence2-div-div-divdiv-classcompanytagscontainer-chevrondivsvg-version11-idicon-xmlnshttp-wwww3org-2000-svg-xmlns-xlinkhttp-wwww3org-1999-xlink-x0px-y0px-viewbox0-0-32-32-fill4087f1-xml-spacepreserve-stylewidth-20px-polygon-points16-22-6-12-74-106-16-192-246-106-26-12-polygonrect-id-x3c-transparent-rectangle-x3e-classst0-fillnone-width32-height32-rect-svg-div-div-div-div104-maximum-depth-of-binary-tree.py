# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        maxdepth = float("-inf")
        def recur(node):
            nonlocal depth
            nonlocal maxdepth
            if not node:
                return 0
            depth += 1
            if not node.left and not node.right:
                maxdepth = max(depth, maxdepth)
            recur(node.left)
            recur(node.right)
            depth -= 1
        recur(root)
        return maxdepth