class Solution:
    def list_of_digits(self, num):
        x = []
        while num:
            x.append(num % 10)
            num = int(num / 10)
        
        #print(x)
        return x
    def addDigits(self, num: int) -> int:
        summ = num
        while summ >= 10:
            summ = sum(self.list_of_digits(summ))
            #print(self.list_of_digits(summ), summ)
        
        return summ
        
