def permutex(elements):
    # Base case: if there's only one element, return it as the only permutation
    if len(elements) == 1:
        return [elements]
    
    # List to store all permutations
    permutations = []
    
    # Iterate over the array and fix each element at the first position
    for i in range(len(elements)):
        first = elements[i]
        # Remaining elements after removing the fixed element
        remaining_elements = elements[:i] + elements[i+1:]
        
        # Recursively find permutations of the remaining elements
        for p in permutex(remaining_elements):
            permutations.append([first] + p)
    
    return permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutex(nums)
        
