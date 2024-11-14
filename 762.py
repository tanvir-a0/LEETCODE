class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Set of prime numbers up to 20 (since set bits count in binary up to 10^6 is <= 20)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        def is_prime_set_bits(num):
            # Count set bits in the binary representation
            set_bits = bin(num).count('1')
            # Check if the count of set bits is in the set of primes
            return set_bits in primes

        # Count numbers in the range [left, right] with a prime number of set bits
        return sum(1 for num in range(left, right + 1) if is_prime_set_bits(num))
