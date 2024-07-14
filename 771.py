class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = [x for x in jewels]
        s = [x for x in stones]

        print(j,s)
        count = 0
        for element in s:
            if element in j:
                count = count + 1
        
        return count
        