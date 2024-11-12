from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        temp_li = []
        for d in digits:
            temp_li.append(num_dict[d])
        print(temp_li)


        if len(temp_li) == 0:
            return []
        

        ans = [''.join(combo) for combo in product(*temp_li)]

        return ans
        b
