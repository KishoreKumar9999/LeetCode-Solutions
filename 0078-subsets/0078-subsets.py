import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, curr):
            
            if i >= len(nums):
                res.append(curr[:])
                return
            # Not include 
            backtrack(i+1,curr)
            print(curr)
            # include
            curr.append(nums[i])
            backtrack(i+1, curr)
            print(curr)
            curr.pop()
            
            
            
        backtrack(0, [])
        return res
    
       