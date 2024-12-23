class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        print(nums1)
        for ii in nums1:
            if ii in nums2:
                return ii
        
        if nums1[0]*10+nums2[0] >  nums1[0]+nums2[0]*10:
            return nums1[0]+nums2[0]*10
            
        return nums1[0]*10+nums2[0]
