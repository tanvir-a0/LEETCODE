class Solution:
    def checkString(self, s: str) -> bool:
        ss = list(s)

        for i in range(1,len(ss)):
            print(ss[0:i], ss[i: len(ss)])
            if 'b' in ss[0:i] and 'a' in ss[i: len(ss)]:
                return False
        return True
