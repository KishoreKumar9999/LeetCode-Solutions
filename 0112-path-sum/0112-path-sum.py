# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0
        a = 0
        if not root and targetSum == 0:
            return False
        def recur(node):
            nonlocal sum
            nonlocal a
            if not node:
                return 
            sum += node.val
            print(sum, "node.val", node.val)
            if node.left == None and node.right == None:
                print(sum, targetSum)
                if sum == targetSum:
                    a= True
                else:
                    if a != True:
                        a = False
            recur(node.left)
            recur(node.right)
            sum -= node.val
            return a
        recur(root)
        return a
        