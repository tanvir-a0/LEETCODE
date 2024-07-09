class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:]
        count1 = 0
        for element in binary_str:
            if element == "1":
                count1 = count1 + 1
        return count1
        