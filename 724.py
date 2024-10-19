class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = -1
        for i in range(0,len(nums)+1):
            #print(nums[:i], sum(nums[:i]), nums[i+1:], sum(nums[i+1:]))
            if sum(nums[:i]) == sum(nums[i+1:]):
                ans = i
                if ans > len(nums) - 1:
                    ans = -1
                break
        return ans
