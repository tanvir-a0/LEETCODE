class Solution:
    def kthCharacter(self, k: int) -> str:
        count = 0
        word = ['a']

        while count < k:
            temp = []
            for i, c in enumerate(word):
                if c == 'z':
                    temp.append('a')
                else:
                    temp.append(chr(ord(c)+1))
            
            word.extend(temp)
            count += len(temp)

        return word[k-1]
