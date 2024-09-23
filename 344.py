class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)):
            s[i], s[int(len(s)) - i - 1] = s[int(len(s)) - i - 1] , s[i]