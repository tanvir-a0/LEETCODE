import copy

class Solution:
    def find_val(self, i,j,mat):
        row = len(mat)
        col = len(mat[0])
        if i >= row or i < 0:
            return -1
        if j >= col or j < 0:
            return -1
        #print("returning: ", mat[i][j], "i:", i, "j:", j, "mat:", mat)
        return mat[i][j]
    
    def return_list(self, row, col, mat):
        lst = []
        lst.append(self.find_val(row, col, mat))
        lst.append(self.find_val(row + 1, col, mat))
        lst.append(self.find_val(row - 1, col, mat))
        lst.append(self.find_val(row, col + 1, mat))
        lst.append(self.find_val(row, col - 1, mat))
        lst.append(self.find_val(row + 1, col + 1, mat))
        lst.append(self.find_val(row - 1, col - 1, mat))
        lst.append(self.find_val(row + 1, col - 1, mat))
        lst.append(self.find_val(row - 1, col + 1, mat))

        val = len(lst) - lst.count(-1)
        lst = [0 if num == -1 else num for num in lst]
        smoothed_value = int(sum(lst) / val)  
        return smoothed_value

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result_img = copy.deepcopy(img)  
        for row in range(len(img)):
            for col in range(len(img[0])):
                result_img[row][col] = self.return_list(row, col, img)
        
        return result_img

        
