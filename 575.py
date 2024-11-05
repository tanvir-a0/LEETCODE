class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(int(len(candyType)/2), int(len(set(candyType))))
