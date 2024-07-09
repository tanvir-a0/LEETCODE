class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_str = ""
        for element in s:
            if element >= "A" and element <= "Z":
                temp_str = temp_str + element
            if element >= "a" and element <= "z":
                temp_str = temp_str + element
        temp_str = temp_str.lower()
        for i in range(len(temp_str)):
            if temp_str[i] != temp_str[len(temp_str) - i - 1]:
                return False

        print(temp_str)
        return True
        