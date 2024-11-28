class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dictt = {}
        for c in nums:
            if c not in dictt:
                dictt[c] = 1
            else:
                dictt[c] = dictt[c] + 1
        
        degree = max(list(dictt.values()))
        #print("degree: ", degree, dictt)

        if degree == 1:
            return 1
        
        num_degree = []
        for key, value in dictt.items():
            if value == degree:
                num_degree.append(key)
        
        ans = len(nums)
        for c in num_degree:
            li = nums.index(c)
            ri = len(nums) - nums[::-1].index(c)
            ans = min(ans, ri-li )
        return ans
        
