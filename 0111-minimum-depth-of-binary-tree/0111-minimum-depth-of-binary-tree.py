# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth, mindepth = 0, float("inf")
        def recur(node):
            nonlocal depth
            nonlocal mindepth
            if node == None:
                return 0
            depth += 1
            if node.left == None and node.right == None:
                mindepth = min(depth, mindepth)
            recur(node.left)
            recur(node.right)
            depth -= 1
        recur(root)
        return mindepth
        
        