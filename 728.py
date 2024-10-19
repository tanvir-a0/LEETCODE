class Solution:
    def check_self_divide(self, num = 1):
        if "0" in str(num):
            return False
        for c in str(num):
            if num % int(c) == 0:
                continue
            else:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            #print(i, self.check_self_divide(num = i))
            if self.check_self_divide(num = i):
                ans.append(i)
        return ans
        
        
