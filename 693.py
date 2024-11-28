class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bina = bin(n)[2:]
        #print(bina)

        
        for i in range(len(bina)-1):
            #print(bina[i] == bina[i+1])
            if bina[i] == bina[i+1]:
                return False
        
        return True
