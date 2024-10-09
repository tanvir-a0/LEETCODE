class Solution:
    def convertToBase7(self, num: int) -> str:
        solution_str = ""

        if num  == 0:
            return "0"
        
        nc = num
        if num < 0:
            nc = -num
        while True:
            print(nc, nc//7, nc%7)
            solution_str = solution_str + str(nc%7)
            nc = nc//7

            if nc < 7:
                solution_str = solution_str + str(nc)
                break
        
        if num < 0:
            solution_str = solution_str + "-"
        solution_str = str(int(solution_str[::-1]))
        

        return solution_str
        
