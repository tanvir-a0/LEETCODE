class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return hex(num)[2:]
        
        num = -num
        binary = bin(num)[2:]
        binary = binary.zfill(32)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2)
        twos_complement = inverted_decimal + 1
        return hex(twos_complement)[2:]
        
        