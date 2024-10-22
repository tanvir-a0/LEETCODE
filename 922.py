class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        result_li = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        for i in range(0, len(nums)):
            if i % 2 == 0:
                result_li.append(even.pop())
            else:
                result_li.append(odd.pop())
        
        return result_li
        
