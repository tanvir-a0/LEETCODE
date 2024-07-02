import time
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        replacing_index = m

        while True:
            print(nums1)

            if i >= m or j >= n:
                break
            
            if nums1[i] <= nums2[j]:
                i = i + 1
            else:
                nums1.insert(i, nums2[j])
                j = j + 1
            
        return nums1


s = Solution()
print(s.merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
# print(s.merge( nums1 = [1], m = 1, nums2 = [], n = 0))
# print(s.merge( nums1 = [0], m = 0, nums2 = [1], n = 1))