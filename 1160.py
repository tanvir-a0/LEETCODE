class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0

        for word in words:
            x = 0
            for c in word:
                #print(word, c,word.count(c), chars.count(c))
                if word.count(c) <= chars.count(c):
                    x = x + 1

            if x == len(word):
                ans = ans + len(word)

            x = 0

        return ans        
