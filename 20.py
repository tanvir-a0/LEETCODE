import time


class Solution(object):
    def isValid(self, s):
        if len(s) == 0 or len(s) == 1:
            return False

        if s == "":
            return True
        if len(s) == 1:
            return False
        if len(s) % 2 == 1:
            return False
        
        opposite = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        sli = [x for x in s]
        i = 0
        while True:
            #time.sleep(2)
            
            current = sli[i]
            next = ""
            if i + 1 >= len(sli):
                break
            else:
                next = sli[i+1]

            #print("sli: ", sli, " current: ",  current, " next: ",  next, " i: ", i)

            if current not in opposite.keys():
                return False


            if opposite[current] == next:
                del sli[i]
                del sli[i]
                i = -1
            
            if len(sli) == 0:
                return True
            
            i = i + 1
        return False
            



            
            

        


s = Solution()
print(s.isValid(s ="(]"))


