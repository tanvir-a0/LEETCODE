class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1_int = 0
        for i in range(len(num1)):
            num_1_int = num_1_int + (ord(num1[i]) - 48) * 10 **(len(num1)  - i - 1)

        num_2_int = 0
        for i in range(len(num2)):
            num_2_int = num_2_int + (ord(num2[i]) - 48) * 10 **(len(num2)  - i - 1)
        
        print(num_1_int, num_2_int)
        #return(num_1_int*num_2_int)
        mul = int(num_1_int*num_2_int)

        # res = ""
        # while(True):
        #     res = res + chr(mul % 10)
        #     mul = mul / 10
        
        # print(mul, res)
        return(str(mul))
        
