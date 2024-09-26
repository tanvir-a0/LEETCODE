class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for p in points:
            x.append(p[0])
        
        widest = 0
        x.sort()
        for i in range(len(x) - 1):
            widest = max(widest, abs(x[i]- x[i+1]))
        
        return widest
        
