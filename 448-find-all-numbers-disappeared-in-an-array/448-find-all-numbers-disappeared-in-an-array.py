class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        print(nums1)
        res = []
        for i in range(1, len(nums)+1):
            print(i, i in nums1)
            if i not in nums1:
                res.append(i)
        return res
        
        