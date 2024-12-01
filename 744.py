class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        print(letters)

        for c in letters:
            if target < c:
                return c

        return letters[0]
