class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0]<nums[-1]:
            for i in range(1, len(nums)):
                ok = nums[i-1]
                if nums[i]>=ok:
                    continue
                else:
                    return False
        else:
            for i in range(1, len(nums)):
                ok = nums[i-1]
                if nums[i]<=ok:
                    continue
                else:
                    return False
        return True
            