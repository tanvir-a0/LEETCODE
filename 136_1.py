class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] = dic[x] + 1
            else:
                dic[x] = 1
        print(dic)
        for x in dic.keys():
            if dic[x] == 1:
                return x
        return 1