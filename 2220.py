class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bstart = bin(start)[2:].zfill(64)  # [2:] is used to remove the '0b' prefix
        gstart = bin(goal)[2:].zfill(64)
        print(gstart,bstart)
        ct = 0
        for i in range(0, 64):
            if bstart[i] != gstart[i]:
                ct = ct + 1
        return ct


        
