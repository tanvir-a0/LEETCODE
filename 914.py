class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dictt = {}
        for element in deck:
            if element in dictt:
                dictt[element] = dictt[element] + 1
            else:
                dictt[element] = 1
            
        maxx = max(list(dictt.values()))
        minn = min(list(dictt.values()))

        if maxx - minn:
            return False
        else:
            return True
