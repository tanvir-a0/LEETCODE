class Solution:
    def isHappy(self, n: int) -> bool:
        nc = n
        while True:
            x = str(nc)
            print(x)
            nc = 0
            for c in x:
                nc = nc + (int(c))**2
            if nc == 1:
                return True
            elif nc < 10:
                return False
                
