from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize dp to store the cumulative path sums for the first row
        dp = [0] * n
        dp[0] = grid[0][0]
        
        # Fill dp for the first row
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        
        # Update dp for each row starting from the second row
        for i in range(1, m):
            # Update the first column in the current row
            dp[0] += grid[i][0]
            for j in range(1, n):
                # For each cell, take the minimum of the top and left cells
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        
        # The last cell of dp now holds the minimum path sum to the bottom-right corner
        return dp[-1]


grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
sol = Solution()
sol.minPathSum(grid)

        