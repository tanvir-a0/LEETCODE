import copy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(97, 123):
            #print(chr(i))
            dic[str(chr(i))] = 0
        #print(dic)

        dic1 = copy.deepcopy(dic)
        dic2 = copy.deepcopy(dic)

        for c in s:
            dic1[c] = dic1[c] + 1
        print(dic1)
        


        for c in t:
            dic2[c] = dic2[c] + 1
        print(dic2)

        return dic1 == dic2

        