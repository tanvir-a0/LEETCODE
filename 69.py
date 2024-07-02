import time


class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        old_mid = 0
        while True:
            mid = (left + right) / 2

            #print(mid)
            #time.sleep(0.1)
            
            if mid < left:
                left = mid

            if ( mid*mid - x ) < 0:
                left = mid

            
            if ( mid*mid - x ) > 0:
                right = mid

            if old_mid == mid:
                return int(mid)
            
            old_mid = mid


s = Solution()
print(s.mySqrt(2**31-1))