class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        licensePlate_x = ""
        for c in licensePlate:
            if c.isalpha():
                licensePlate_x = licensePlate_x + c
        licensePlate = licensePlate_x
        print(licensePlate)

        ans = []
        for word in words:
            word_c = word  # Create a mutable copy of the word
            is_valid = True
            for c in licensePlate:
                if c not in word_c:
                    is_valid = False
                    break
                else:
                    word_c = word_c.replace(c, "", 1)  # Remove only one occurrence of `c`
            if is_valid:
                ans.append(word)  # Add valid word to the result list
        print(ans)
        
        res = ans[0]
        for a in ans:
            if len(a) < len(res):
                res = a
        
        return res
