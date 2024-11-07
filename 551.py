class Solution:
    def checkRecord(self, s: str) -> bool:
        eligable = []
        absent = 0
        for c in s:
            if c == 'A':
                absent = absent + 1
        if absent < 2:
            eligable.append(1)
        else:
            eligable.append(0)

        for i in range(len(s) - 2):
            if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i+2] == 'L':
                eligable.append(0)
        
        print(eligable)
        if 0 in eligable:
            return False
        return True

        
