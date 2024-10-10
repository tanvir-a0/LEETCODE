class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', "A", 'E', "I", 'O', "U"]
        vowels_present = []
        for c in s:
            if c in vowels:
                vowels_present.append(c)
        vowels_swap = vowels_present[::-1]
        print(vowels_present, vowels_swap)

        new_text = ""
        i = 0
        for c in s:
            if c in vowels:
                new_text = new_text + str(vowels_swap[i])
                i = i + 1
            else:
                new_text = new_text + str(c)
        print(new_text)
        return new_text