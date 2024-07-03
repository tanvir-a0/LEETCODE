import time
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        new_li = []
        for element in nums1[:m]:
           new_li.append(element)
        for element in nums2[:n]:
            new_li.append(element)
        
        new_li.sort()
        #print(new_li)

        for i in range(len(new_li)):
            nums1[i] = new_li[i]
        
        return nums1
           


s = Solution()
print(s.merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(s.merge(nums1 = [1], m = 1, nums2 = [], n = 0 ))
print(s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1 ) )
# print(s.merge( nums1 = [2,0], m = 2, nums2 = [1], n = 1))
# print(s.merge( nums1 = [0], m = 0, nums2 = [1], n = 1))