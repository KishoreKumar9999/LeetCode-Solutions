class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            if index == len(nums2)-1:
                res.append(-1)
            for j in range(index, len(nums2)):
                if nums2[j]>nums2[index]:
                    res.append(nums2[j])
                    break
                if nums2[j] == nums2[len(nums2)-1] and nums2[j]<nums2[index]:
                    res.append(-1)
        return res
        