class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        #print(nums1)
        n = len(nums1) - 1

        if n % 2 == 0:
            return nums1[int(n/2)]

        else: 
            return (nums1[int(n/2)] + nums1[int(n/2)+1])/2
        


s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))