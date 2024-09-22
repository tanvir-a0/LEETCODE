class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] = dic[x] + 1

            else:
                dic[x] = 1
        
        max_num = 0
        for x in dic.keys():
            if dic[x] > max_num:
                max_num = dic[x]

        for x in dic.keys():
            if dic[x] == max_num:
                return x


        