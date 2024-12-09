class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dicc = {}
        for x in nums:
            if x in dicc:
                dicc[x] = dicc[x] + 1
            else:
                dicc[x] = 1
            
        for key, value in dicc.items():
            if value %2 != 0:
                return False
        
        return True
