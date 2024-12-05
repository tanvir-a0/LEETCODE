class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False

        dictt = {}
        for element in deck:
            if element in dictt:
                dictt[element] = dictt[element] + 1
            else:
                dictt[element] = 1

        num = dictt[deck[0]]
        for key, value in dictt.items():
            num = math.gcd(num, value)


        return num > 1
