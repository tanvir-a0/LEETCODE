class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        #print(words)

        new_li = []
        for word in words:
            new_li.append(word[::-1])
        
        result = " ".join(new_li)
        #print(result)
        return result
            
        
