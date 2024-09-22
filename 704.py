class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minn = 0
        maxx = len(nums) - 1
        
        old_mid = -1
        while True:
            mid = (minn + maxx)//2
            if old_mid == mid:
                break
            if nums[mid] == target:
                return mid
            elif   target < nums[mid]:
                maxx = mid - 1
            else: 
                minn = mid + 1
            old_mid = mid
        
        return -1


        