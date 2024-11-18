class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        nums = set(nums)
        nums = list(nums)
        l2 = len(nums)
        if l1!=l2:
            return True
        else:
            return False
        