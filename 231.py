class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = abs(n)
        if x == 0:
            return False
        pow = 0
        while True:
            print(x)
            if x == 1:
                break
            if ( x % 2) == 1:
                return False
                
            x = x // 2
            pow = pow + 1

        print("pow",pow)
        if pow % 2 == 0:
            if n < 0:
                return False
            return True
        else:
            if n < 0:
                return False
            else:
                return True

