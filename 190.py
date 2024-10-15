class Solution:
    def reverseBits(self, n: int) -> int:
        rv = bin(n)[2:].zfill(32)
        rv = rv[::-1]
        print(rv)

        return int(rv, 2)
