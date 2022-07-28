class Solution:
    def reverse_array(self, nums, start, end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        # normalizing the k value if it is greater than the length of the array
        if k > length:
            k = k%length
        self.reverse_array(nums, 0, length-1)
        self.reverse_array(nums, 0, k-1)
        self.reverse_array(nums, k, length-1)
        
