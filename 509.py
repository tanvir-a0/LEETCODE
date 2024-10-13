class Solution:
    def fib_iterate(self, num):
        if num == 0:
            return 1
        else:
            return num + self.fib_iterate(num-1)


    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0] * (n+1)
        print(dp)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[n]
        return 0
        
