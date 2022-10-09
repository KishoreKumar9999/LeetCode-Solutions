class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            gtThanLeft = nums[mid] > nums[mid-1] or mid==0
            
            gtThanRight = mid == len(nums)-1 or nums[mid]>nums[mid+1]
            
            if gtThanRight and gtThanLeft:
                return mid
            else:
                if gtThanRight:
                    r = mid-1
                else:
                    l = mid+1
        return -1
                
        
        