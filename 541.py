class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        ans = ""
        while True:
            print(i)
            if i+k >= len(s):
                tmp = s[i:]
                tmp = tmp[::-1]
                ans = ans + tmp
                break
            tmp = s[i:i+k] 
            tmp = tmp[::-1]
            ans = ans + tmp
            #print("flipped: ", tmp)
            
            if i+k+k >= len(s):
                temp1 = s[i+k:]
                ans = ans + temp1
                break
            
            temp1 = s[i+k:i+k+k]
            ans = ans + temp1
            #print("stayed: ", temp1)
            
            i = i + k + k
        
        return ans
      
