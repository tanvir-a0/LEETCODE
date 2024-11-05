class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        x = purchaseAmount % 10
        if x >= 5:
            return 100 - floor(purchaseAmount / 10)*10 - 10
        else:
            return 100 - floor(purchaseAmount / 10)*10 
        
