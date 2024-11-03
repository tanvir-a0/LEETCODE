class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        winners = []
        count = 0

        for i in range(len(pick)):
            print(pick[0:i], pick[i], pick[i+1:])

            if pick[i] in pick[0:i] or pick[i] in pick[i+1:]:
                if pick[i] not in winners:
                    winners.append(pick[i])
                    count = count + 1

        return count
        
