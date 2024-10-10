class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for c1 in nums1:
            for c2 in nums2:
                if c1 == c2:
                    ans.append(c1)
        
        return set(ans)