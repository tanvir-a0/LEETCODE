class Solution(object):
    def minPartitions(self, n):
        max_digit = 0
        for digit in n:
            max_digit = max(max_digit, int(digit))
        return max_digit
