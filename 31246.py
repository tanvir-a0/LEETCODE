class Solution(object):
    def findPermutationDifference(self, s, t):
        count = 0
        for i in range(len(s)):
            count = count + abs( i - t.find(s[i]))

        print(count)
        return count
s = Solution()
s.findPermutationDifference("abc", "abc") # 0
s.findPermutationDifference("abc", "bca") # 2
s.findPermutationDifference("abc", "cab") # 4
s.findPermutationDifference("", "") 