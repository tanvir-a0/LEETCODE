class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        mull = 1

        for c in str(n):
            summ = summ + int(c)
            mull = mull * int(c)
        print(summ, mull)
        return   mull - summ
        
