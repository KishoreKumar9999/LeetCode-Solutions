class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum = 0
        left = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            while sum >= target:
                new_size = (i+1)-left
                res = min(res, new_size)
                sum = sum-nums[left]
                left = left+1
        if res != float('inf'):
            return res
        else:
            return 0