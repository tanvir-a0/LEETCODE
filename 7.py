class Solution:
    def reverse(self, x: int) -> int:
        result_int = 0
        if x < 0:
            result_int = -1*int(str(-1*x)[::-1])
        else:
            result_int = int(str(x)[::-1])
        
        if result_int < -2147483648 or result_int > (2147483648 - 1):
            return 0
        
        return result_int
