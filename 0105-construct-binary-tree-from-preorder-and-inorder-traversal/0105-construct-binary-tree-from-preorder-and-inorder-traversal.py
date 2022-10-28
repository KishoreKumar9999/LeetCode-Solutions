# TC: O(n^2)
# SC: O(h)
# Does this code run on Leetcode: Yes
# Did you find any difficulty in finding the solution: No
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
#         def recur(preorder, inorder):
#             if not preorder and not inorder:
#                 return None
#             root = TreeNode(preorder[0])
#             mid = inorder.index(root.val)
#             print(mid)
#             root.left = recur(preorder[1:mid+1], inorder[:mid])
#             root.right = recur(preorder[mid+1:], inorder[mid+1:])
#             return root
#         return recur(preorder, inorder)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recur(preorder, inorder):
            mapping = {}
            for i,v in enumerate(inorder):
                mapping[v] = i
            if not preorder and not inorder:
                return None
            root = TreeNode(preorder[0])
            mid = mapping[root.val]
            print(mid)
            root.left = recur(preorder[1:mid+1], inorder[:mid])
            root.right = recur(preorder[mid+1:], inorder[mid+1:])
            return root
        return recur(preorder, inorder)
        
