class Solution(object):
    def maxNumberOfBalloons(self, text):
        balloon = "balloon"
        b = defaultdict(int)
        for c in text:
            if c in balloon:
                b[c] = b[c] + 1
        
        if any(c not in b for c in balloon):
            return 0
        
        return min(b['b'], b['a'], b['l']//2, b['o']//2 , b['n'])
                
        
