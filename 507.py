def find_divisors(n): 
    divisors = [] 
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:  # Check if i is a divisor 
            divisors.append(i) 
            if i != n // i:  # Avoid adding the square root twice 
                divisors.append(n // i) 
    return sorted(divisors) 



class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        print(find_divisors(num),  sum(find_divisors(num) ))
        if sum(find_divisors(num) ) - num == num:
            return True

        return False
        
