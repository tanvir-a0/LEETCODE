class Solution(object):
    def addBinary(self, a, b):
        a_int = 0
        b_int = 0

        for i in range(len(a)):
            a_int = a_int + int(a[i]) * 2 ** (len(a) - 1 - i)
        #print(a_int)


        for i in range(len(b)):
            b_int = b_int + int(b[i]) * 2 ** (len(b) - 1 - i)
        #print(b_int)

        result_int = a_int + b_int
        #print(result_int)

        result_str = ""
        while True:
            result_str = result_str + str(result_int % 2)
            result_int = result_int // 2
            if result_int == 0:
                break
        
        return result_str[::-1]

        
s = Solution()
print(s.addBinary(a = "11", b = "1"))
print(s.addBinary(a = "1010", b = "1011"))
print(s.addBinary(a = "0", b = "0"))
print(s.addBinary(a = "", b = ""))