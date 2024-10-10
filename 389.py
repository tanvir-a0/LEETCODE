class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        if t == "":
            return s
        
        s_dic = {}
        if len(s) > len(t):
            s, t = s, t
        else:
            s, t = t, s

        for c in s:
            if c in s_dic:
                s_dic[c] = s_dic[c] + 1
            else:
                s_dic[c] = 1
        for c in t:
            if c in s_dic:
                s_dic[c] = s_dic[c] - 1
        
        for key, value in s_dic.items():
            if value == 1:
                return key
        
        print(s_dic)
        
        
