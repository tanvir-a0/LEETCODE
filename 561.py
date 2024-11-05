class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        sorted_list = sorted_list[::-1]
        print(sorted_list)

        ans = 0
        i = 0
        while True:
            ans = ans + min(sorted_list[i], sorted_list[i+1])
            i = i + 2
            if i >= len(nums):
                break
        
        return ans
        
