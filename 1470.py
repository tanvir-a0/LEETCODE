class Solution(object):
    def shuffle(self, nums, n):
        new_li = []
        for i in range(n):
            new_li.append(nums[i])
            new_li.append(nums[n+i])
        
        return new_li
        
