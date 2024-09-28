class Solution:
    def repeatedCharacter(self, s: str) -> str:
        temp_dic = {

        }
        def check_dic(temp_dic = temp_dic):
            for x in temp_dic.keys():
                print(x)
                if temp_dic[x] >= 2:
                    return x
            return None

        for i in range(len(s)):
            if s[i] in temp_dic:
                temp_dic[s[i]] = temp_dic[s[i]] + 1
            else:
                temp_dic[s[i]] = 1

            if check_dic(temp_dic) != None:
                return check_dic(temp_dic)
            print(temp_dic)
