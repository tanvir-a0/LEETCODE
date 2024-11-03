class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = 0
        for command in commands:
            if command == "RIGHT":
                res = res + 1
            if command == "UP":
                res = res - n
            if command == "DOWN":
                res = res + n
            if command == "LEFT":
                res = res - 1

        return res        
