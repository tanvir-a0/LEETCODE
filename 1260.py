def list_to_matrix(lst, rows, cols):
    if len(lst) != rows * cols:
        raise ValueError("List size does not match the specified grid dimensions")
    return [lst[i * cols:(i + 1) * cols] for i in range(rows)]

def right_shift(lst, steps=1):
    steps %= len(lst) 
    return lst[-steps:] + lst[:-steps]

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        plain = []
        for row in grid:
            for element in row:
                plain.append(element)
        
        plain = right_shift(plain, k)
        return list_to_matrix(plain, len(grid), len(grid[0]))

        


        

        
