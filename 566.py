class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        single_row = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                single_row.append(mat[i][j])
        
        print(single_row)

        result_row = []

        if(len(single_row) != r*c):
            return mat

        count = 0
        for i in range(r):
            result_row.append([])
            for j in range(c):
                print(count)
                result_row[i].append(single_row[count])
                count = count + 1
        print(result_row)
        return result_row
        
