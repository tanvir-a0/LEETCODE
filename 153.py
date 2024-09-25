class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return nums[0]
        l,r = 0, len(nums) - 1
        mid = 0
        previous_mid = 0
        minn = float("inf")
        while l <= r:
            
            mid = (l+r)//2
            minn = min(nums[mid], nums[l], nums[r])
            if nums[mid] > nums[r]:
                l = mid + 1
                minn = min(nums[mid], nums[l], nums[r])

            else: 
                r = mid
                minn = min(nums[mid], nums[l], nums[r])
            
            if previous_mid == mid:
                break
            
            previous_mid = mid
        
        return minn
