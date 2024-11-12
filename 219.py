class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chekced = {

        }

        for i in range(len(nums)):
            if nums[i] in chekced and abs(chekced[nums[i]] - i) <= k:
                return True
            else:
                chekced[nums[i]] = i
        
        return False
