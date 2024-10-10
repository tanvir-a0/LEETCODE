class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        num = 1
        while(num <= (2**31-1)):
            if num == n:
                return True
            
            num = num * 4
        
        if num == n:
            return True
        
        return False
        