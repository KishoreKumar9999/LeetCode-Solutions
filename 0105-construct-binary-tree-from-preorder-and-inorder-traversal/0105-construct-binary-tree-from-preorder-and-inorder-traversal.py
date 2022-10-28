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

# TC: O(n)
# SC: O(n)
# Does this code run on Leetcode: Yes
# Did you find any difficulty in finding the solution: No

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_mapping = {}
        for k,v in enumerate(inorder):
            inorder_index_mapping[v] = k
        index = 0
        def buildtree(left,right):
            nonlocal index
            if left>right:
                return None
            root_val=preorder[index]
            root = TreeNode(root_val)
            index+=1
            root.left = buildtree(left, inorder_index_mapping[root_val]-1)
            root.right = buildtree(inorder_index_mapping[root_val]+1, right)
            return root
        return buildtree(0, len(preorder)-1)
        
