class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = {}
        for x in list1:
            if x in list2:
                result[x] = list1.index(x) + list2.index(x)
        

        ret = []
        miin = float('inf')
        for s, v in result.items():
            if v < miin:
                miin = v
        
        for s, v in result.items():
            if v == miin:
                ret.append(s)

        return ret
        
