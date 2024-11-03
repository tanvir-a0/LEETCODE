class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def find_index(self, value):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == value:
                    return (i,j)
        

    def adjacentSum(self, value: int) -> int:
        row_cols = len(self.grid) #this will be 3 for example 1
        to_sum = []
        i, j = self.find_index(value)
        print("neighbors value i j " , value, i,j)
        if i - 1 < 0:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i-1][j])
        if i + 1 >= row_cols:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i+1][j])
        if j - 1 < 0:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i][j-1])
        if j + 1 >= row_cols:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i][j+1])
        
        print("neighbors value: ", value, " sum: ", sum(to_sum))
        return sum(to_sum)
        

    def diagonalSum(self, value: int) -> int:
        row_cols = len(self.grid) #this will be 3 for example 1
        to_sum = []
        i, j = self.find_index(value)
        print("diagonal value i j " , value, i,j)
        if i - 1 < 0 or j - 1 <0:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i-1][j-1])
        if i + 1 >= row_cols or j + 1 >= row_cols:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i+1][j+1])
        if i - 1 < 0 or j + 1 >= row_cols:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i-1][j+1])
        if i + 1 >= row_cols or j - 1 < 0:
            to_sum.append(0)
        else:
            to_sum.append(self.grid[i+1][j-1])
        
        print("diagonal value: ", value, " sum: ", sum(to_sum), to_sum)
        return sum(to_sum)
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
