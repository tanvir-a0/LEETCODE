class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return_grid = []
        for i in range(len(grid)-2):
            return_grid.append([])
            for j in range(len(grid)-2):
                return_grid[i].append(None)
        print(return_grid)

        def return_value(i, j, grid):
            maxx = 0
            for x in range(i,i+3):
                for y in range(j, j+3):
                    #maxx = max(maxx, grid[i][j])
                    print("x:", x, "y:", y)
                    maxx = max(maxx, grid[x][y])
                    pass
            return maxx


        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                print(return_value(i,j, grid))
                return_grid[i][j] = return_value(i,j, grid)
                #print("i:", i, "j:", j)
                
        return return_grid
        