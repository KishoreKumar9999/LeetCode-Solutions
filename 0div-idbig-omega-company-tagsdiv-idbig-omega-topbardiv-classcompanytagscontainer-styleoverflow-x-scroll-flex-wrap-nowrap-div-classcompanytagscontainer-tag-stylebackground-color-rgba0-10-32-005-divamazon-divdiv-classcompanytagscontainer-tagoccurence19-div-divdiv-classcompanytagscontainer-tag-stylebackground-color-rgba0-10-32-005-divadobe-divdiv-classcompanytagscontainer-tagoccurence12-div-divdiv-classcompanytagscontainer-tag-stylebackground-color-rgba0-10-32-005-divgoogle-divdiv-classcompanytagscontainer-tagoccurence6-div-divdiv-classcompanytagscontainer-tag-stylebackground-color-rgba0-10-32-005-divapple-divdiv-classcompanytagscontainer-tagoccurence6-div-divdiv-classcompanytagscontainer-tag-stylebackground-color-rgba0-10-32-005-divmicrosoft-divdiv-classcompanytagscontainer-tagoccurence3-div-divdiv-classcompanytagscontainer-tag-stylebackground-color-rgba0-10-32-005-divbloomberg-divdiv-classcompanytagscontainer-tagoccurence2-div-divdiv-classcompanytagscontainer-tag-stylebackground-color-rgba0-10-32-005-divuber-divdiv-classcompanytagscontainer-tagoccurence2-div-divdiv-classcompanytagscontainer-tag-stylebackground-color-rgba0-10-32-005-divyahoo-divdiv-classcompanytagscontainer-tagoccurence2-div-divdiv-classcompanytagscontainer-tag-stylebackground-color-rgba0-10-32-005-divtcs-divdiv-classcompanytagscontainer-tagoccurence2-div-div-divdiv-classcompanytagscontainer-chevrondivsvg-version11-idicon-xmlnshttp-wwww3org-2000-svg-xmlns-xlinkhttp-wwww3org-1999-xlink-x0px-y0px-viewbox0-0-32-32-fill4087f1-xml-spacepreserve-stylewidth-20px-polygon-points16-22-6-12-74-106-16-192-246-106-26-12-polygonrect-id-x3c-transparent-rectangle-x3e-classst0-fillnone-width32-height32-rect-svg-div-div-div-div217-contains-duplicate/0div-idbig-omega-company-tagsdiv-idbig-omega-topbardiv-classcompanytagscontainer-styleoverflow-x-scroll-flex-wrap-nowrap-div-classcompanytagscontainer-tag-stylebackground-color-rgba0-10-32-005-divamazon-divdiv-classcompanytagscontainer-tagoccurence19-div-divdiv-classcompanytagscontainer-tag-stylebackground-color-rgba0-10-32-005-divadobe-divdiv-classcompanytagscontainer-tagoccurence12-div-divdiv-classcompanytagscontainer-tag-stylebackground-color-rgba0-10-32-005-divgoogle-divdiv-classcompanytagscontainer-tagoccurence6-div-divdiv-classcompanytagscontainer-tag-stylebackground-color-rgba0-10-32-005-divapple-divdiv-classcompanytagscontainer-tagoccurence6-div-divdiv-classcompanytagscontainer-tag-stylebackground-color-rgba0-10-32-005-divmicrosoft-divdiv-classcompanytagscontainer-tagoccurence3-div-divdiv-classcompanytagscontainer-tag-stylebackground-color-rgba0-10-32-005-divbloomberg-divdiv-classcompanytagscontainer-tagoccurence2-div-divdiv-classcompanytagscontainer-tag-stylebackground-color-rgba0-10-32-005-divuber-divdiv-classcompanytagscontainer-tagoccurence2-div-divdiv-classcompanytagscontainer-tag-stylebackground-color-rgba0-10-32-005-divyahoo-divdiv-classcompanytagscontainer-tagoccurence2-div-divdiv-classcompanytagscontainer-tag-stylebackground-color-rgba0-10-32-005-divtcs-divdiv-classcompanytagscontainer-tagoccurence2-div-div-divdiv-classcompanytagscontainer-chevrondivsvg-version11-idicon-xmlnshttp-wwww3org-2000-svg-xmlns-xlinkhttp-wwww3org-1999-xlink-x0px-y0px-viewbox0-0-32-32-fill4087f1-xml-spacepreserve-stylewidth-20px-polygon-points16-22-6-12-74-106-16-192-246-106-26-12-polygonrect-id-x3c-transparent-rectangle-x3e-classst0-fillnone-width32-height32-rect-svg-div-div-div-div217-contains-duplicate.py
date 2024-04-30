class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for i in range(len(nums)):
            if nums[i] in c:
                return True
            
            else:
                c.add(nums[i])
        return False