class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 0:
            return False
        
        n_old = n
        while True:
            if n % 2 == 0: n = int(n / 2)
            if n % 3 == 0: n = int(n / 3)
            if n % 5 == 0: n = int(n / 5)

            if n_old == n:
                break
            n_old = n
        
        if n == 1:
            return True
        else:
            return False
        
