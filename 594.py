class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        max_length = 0
        for num in frequency:
            if num + 1 in frequency:
                max_length = max(max_length, frequency[num] + frequency[num + 1])
        
        return max_length
