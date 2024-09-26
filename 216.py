import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        elements = []
        for i in range(1, int(n)):
            elements.append(i)
        #print(elements)
        combinations = list(itertools.combinations(elements, k))
        result = []
        for combination in combinations:
            if sum(combination) == n:
                result.append(combination)
        print(combinations)

        return result
        
