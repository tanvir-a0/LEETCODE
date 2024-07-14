class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        if len(accounts) == 0:
            return 0

        for i in range(0, len(accounts)):
            su = sum(accounts[i]) 
            maxx = max(maxx, su)
        
        return maxx
        