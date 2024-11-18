class Solution:
    def grayCode(self, n: int) -> List[int]:

        gray_code = [0]
        for i in range(n):
            # Reflect the current list and add 1 << i to each reflected element
            reflected = [x + (1 << i) for x in reversed(gray_code)]
            gray_code += reflected
        return gray_code
        
