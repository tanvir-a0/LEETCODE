class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0
        for i in range(1, n+1):
            if i % m != 0:
                print(i)
                num1 = num1 + i
        print("_________")
        num2 = 0
        for i in range(1,n+1):
            if i % m == 0:
                print(i)
                num2 = num2 + i
        
        return num1 - num2

        
