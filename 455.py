class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()
        
        # Initialize pointers for children and cookies
        i, j = 0, 0
        
        # Iterate through cookies and children
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If cookie can satisfy the child
                i += 1       # Move to the next child
            j += 1           # Move to the next cookie
        
        # The number of satisfied children
        return i

        
