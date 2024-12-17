def remove_duplicates(s):
    result = ''
    seen = set()
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dictt = {}
        key = key.replace(" ", "")
        key = remove_duplicates(key)
        #print("key: ", key)
        for i in range(0,26):
            #print(i, chr(i+97))
            if key[i] in dictt:
                i = i - 1
                continue
            dictt[key[i]] = chr(i+97)
        #print(dictt)

        res = ""
        for c in message:
            if c in dictt:
                res = res + dictt[c]
            else:
                res = res + " "
        
        return res

        
