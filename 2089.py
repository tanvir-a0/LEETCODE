class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        print(nums)

        res = []
        i = 0
        for c in nums:
            if c == target:
                res.append(i)
            i = i + 1

        return res


        
