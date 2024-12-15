class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        if len(nums) == 1:
            return True

        lst = []
        previous = 0
        current = 0
        while True:
            if nums[current] == 1:
                lst.append(current - previous -1)
                previous = current
            
            current = current + 1
            if current >= len(nums):
                break

        if len(lst) <= 1:
            return True
        print(lst[1:])
        return min(lst[1:]) >= k

        
