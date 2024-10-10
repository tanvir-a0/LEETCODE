import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False

        i = 0
        while True:
            if 3**i > 2**31 - 1:
                break
            if 3**i == n:
                return True
            i = i + 1
        return False





        