class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        char_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

        res = {}
        for word in  words:
            res[word] = ""
            for c in word:
                res[word] = res[word] + char_to_morse[c]
        
        #print(res)
        transformations = set(list(res.values()))
        #print(transformations)
        return(len(transformations))
