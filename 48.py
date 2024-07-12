class Solution:
    def vertical_flip(self, mat):
        row = len(mat)
        col = len(mat[0])
        new_matrix = []
        for i in range(row):
            new_matrix.append([])
            for j in range(col):
                new_matrix[i].append(None)
        #print(new_matrix)

        for i in range(row):
            for j in range(floor(col)):
                new_matrix[i][col - 1 - j] = mat[i][j]
        return new_matrix

    def transpose(self, mat):
        row = len(mat)
        col = len(mat[0])
        new_matrix = []
        for i in range(row):
            new_matrix.append([])
            for j in range(col):
                new_matrix[i].append(None)
        #print(new_matrix)

        for i in range(row):
            for j in range(col):
                new_matrix[j][i] = mat[i][j]
        return new_matrix

                

    def rotate(self, matrix: List[List[int]]) -> None:
        if matrix == [[]]:
            return [[]]

        print(matrix)
        print("transpose: ", self.transpose(matrix))
        print("flipped: ", self.vertical_flip(self.transpose(matrix)))
        temp_mat = self.vertical_flip(self.transpose(matrix))
        row = len(temp_mat)
        col = len(temp_mat[0])
        for i in range(row):
            for j in range(floor(col)):
                matrix[i][j] = temp_mat[i][j]
        return matrix
        