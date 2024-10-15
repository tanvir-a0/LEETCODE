class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        #case 1
        temp = 0
        for x in word:
            if x.isupper():
                temp = temp + 1
        if temp == len(word):
            return True
        
        temp = 0
        for x in word:
            if x.islower():
                temp = temp + 1
        if temp == len(word):
            return True
        

        temp = 0
        for x in word[1:]:
            if x.islower():
                temp = temp + 1
        if temp == len(word)-1 and word[0].isupper():
            return True

        return False
        
        
