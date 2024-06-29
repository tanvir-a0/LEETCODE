class Solution(object):
    def romanToInt(self, s):
        values = {
            "I":  1,
            "V":  5,
            "X":  10,
            "L":  50,
            "C":  100,
            "D":  500,
            "M":  1000
        }
        li = [x for x in s]
        vli = []
        #print(li)
        for element in li:
            vli.append(values[element])
        i = 0
        result = 0
        while True:
            if i >= len(vli):
                break

            current_value = vli[i]
            next_value = 0
            if i == len(vli) - 1:
                next_value = 0
            else:
                next_value = vli[i + 1]
            
            if current_value >= next_value:
                result = result + current_value 
            else:
                result = result + next_value - current_value
                i = i + 1
            
            i = i + 1


        return result
        

s = Solution()
print(s.romanToInt(s = "MCMXCIV"))