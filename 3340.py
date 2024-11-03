class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0

        for i in range(len(num)):
            if i % 2 == 0:
                even = even + int(num[i])
            else:
                odd = odd + int(num[i])

        return odd == even


