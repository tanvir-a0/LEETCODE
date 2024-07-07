class Solution(object):
    def findWordsContaining(self, words, x):
        temp = []
        for i in range(len(words)) :
            if x in words[i]:
                temp.append(i)
        
        return temp
