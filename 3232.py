class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        all_single_sum = 0
        all_double_sum = 0

        for x in nums:
            if x < 10:
                all_single_sum = all_single_sum + x
            else:
                all_double_sum = all_double_sum + x
        
        print(all_single_sum, all_double_sum)
        if all_single_sum == all_double_sum:
            return False
        
        return TrueZ
