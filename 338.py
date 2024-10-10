class Solution:
    def countBits(self, n: int) -> List[int]:
        x = [p for p in range(0, n+1)]
        print(x)

        ans = []
        for i in x:
            ans.append(bin(i)[2:].count("1"))
        print(ans)
        return ans