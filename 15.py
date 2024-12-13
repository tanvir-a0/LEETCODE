class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:
                last_two_sum = nums[left] + nums[right]

                if last_two_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right-1]:
                        right = right - 1
                    left = left + 1
                    right = right + 1
                
                if last_two_sum < target:
                    left = left + 1
                else:
                    right = right - 1
        
        return res
