class Solution:
    def list_of_digits(self, num):
        x = []
        while num:
            x.append(num % 10)
            num = int(num / 10)
        
        return x
    def addDigits(self, num: int) -> int:
        temp_li = self.list_of_digits(num)
        while sum(temp_li) >= 10:
            temp_li = self.list_of_digits(num)
            num = sum(temp_li)
        
        return num
        
