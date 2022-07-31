class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        mid = int(r/2)
        res = []
        # Finding lower index
        while l<=r:
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
            mid = l+(r-l)//2
        if l<len(nums) and nums[l]==target:
            res.append(l)
        else:
            res.append(-1)
        # Finding higher index    
        l, r = 0, len(nums)-1
        mid = int(r/2)
        while l<=r:
            if nums[mid]<=target:
                l = mid+1
            else:
                r = mid-1
            mid = l+(r-l)//2
        if r==-1:
            res.append(r)
        elif r<len(nums) and nums[r]==target:
            res.append(r)
        else:
            res.append(-1)
            
        return res
        
        