import re
def get_words_from_paragraph(paragraph: str) -> list:
    # Use regex to extract words (alphanumeric strings) from the paragraph
    words = re.findall(r'\b\w+\b', paragraph)
    return words

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = get_words_from_paragraph(paragraph)
        word_c = [w.lower() for w in words]
        words = word_c

        word_count = {}
        for word in words:
            if word in banned:
                continue
            
            if word in word_count:
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1
        
        print(word_count)
        ans = ""
        maxx =  max(list(word_count.values()))
        for key,value in word_count.items():
            if value == maxx:
                ans = key
        
        return ans
