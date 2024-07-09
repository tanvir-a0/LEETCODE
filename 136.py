class Solution(object):
    def singleNumber(self, nums):
        nums_copy = nums
        while len(nums_copy) != 0:
            temp = nums_copy.pop(0)
            print(nums_copy)
            if temp in nums_copy:
                nums_copy.remove(temp)
                continue
            else:
                return temp

        
