import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i):
            
            if i >= len(nums):
                res.append(curr[:])
                return
            # Not include 
            backtrack(i+1)
            # include
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            
            
            
        backtrack(0)
        return res
    
       