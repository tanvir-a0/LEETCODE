class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dictt = {}

        for x in paths:
            dictt[x[0]] = x[1]

        current = paths[0][0]

        while current in list(dictt.keys()):
            current = dictt[current]
        
        return current
        
