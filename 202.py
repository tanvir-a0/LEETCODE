class Solution:
    def isHappy(self, n: int) -> bool:
        nc = n

        cycle = 100
        already_got = []
        while True:
            x = str(nc)
            print(x, nc)
            already_got.append(nc)
            nc = 0
            for c in x:
                nc = nc + (int(c))**2
                
            x = str(nc)
            print(x, nc)

            if nc == 1:
                return True

            if nc in already_got:
                return False
            
                
