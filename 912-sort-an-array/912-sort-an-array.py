# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.quick_sort_rec(nums, 0, len(nums)-1)
#         return nums
    
#     def quick_sort_rec(self,nums, low, high):
#         if high > low:
#             # pivot_index is the partitioning index
#             pivot_index = self.partition(nums, low, high)

#             # Sort elements before partition
#             self.quick_sort_rec(nums, low, pivot_index - 1)
#             # Sort elements after partition
#             self.quick_sort_rec(nums, pivot_index + 1, high)
#     def partition(self, nums, low, high):

#     # Initializing pivot's index to low
#         pivot_value = nums[low]
#         i = low
#         j = high

#     # Loop till i pointer crosses j pointer
#         while i < j:

#             # Increment the 'i' pointer till it finds an element greater than pivot
#             while i <= j and nums[i] <= pivot_value:
#                 i += 1

#             # Decrement the 'j' pointer till it finds an element less than pivot
#             while nums[j] > pivot_value:
#                 j -= 1

#             # Swap the numbers on 'i' and 'j'
#             if i < j:
#                 nums[i], nums[j] = nums[j], nums[i]

#         # Swap pivot element with element on 'j' pointer.
#         nums[low], nums[j] = nums[j], pivot_value

#         # return the pivot index
#         return j
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(N), min(N), max(N), []
        for n in range(m,M+1): S.extend([n]*C[n])
        return S
		
    
        
        