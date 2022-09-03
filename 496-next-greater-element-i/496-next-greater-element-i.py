# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for i in range(len(nums1)):
#             index = nums2.index(nums1[i])
#             if index == len(nums2)-1:
#                 res.append(-1)
#             for j in range(index, len(nums2)):
#                 if nums2[j]>nums2[index]:
#                     res.append(nums2[j])
#                     break
#                 if nums2[j] == nums2[len(nums2)-1] and nums2[j]<nums2[index]:
#                     res.append(-1)
#         return res
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        hashmap = {}
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        print(stack)
        print(hashmap)
        while stack:
            hashmap[stack.pop()] = -1
        print(stack)
        print(hashmap)
        res = []
        for i in range(len(nums1)):
            res.append(hashmap[nums1[i]])
        return res
            
        