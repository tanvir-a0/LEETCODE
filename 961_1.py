class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = int(len(nums) / 2)

        dictt = {}
        for element in nums:
            if element in dictt:
                dictt[element] = dictt[element] + 1
            else:
                dictt[element] = 1
        
        #print(dictt)

        for key, value in dictt.items():
            if value == n:
                return key
        
