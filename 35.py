class Solution(object):
    def searchInsert(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        while True:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if left == right:
                return left if nums[left] > target else left + 1
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle


s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
        