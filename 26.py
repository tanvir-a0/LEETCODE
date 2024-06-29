class Solution(object):
    def removeDuplicates(self, nums):
        #print(nums)
        end = len(nums) - 1
        i = 0
        count = 0
        while True:
            #print(nums)
            #time.sleep(2)
            if i == end:
                break
            
            if i+1 >= len(nums):
                break

            if nums[i] == nums[i+1]:
                del nums[i+1]
                nums.append("_")
                count = count + 1
                end = end - 1
                continue
            
            i = i + 1

        return count, nums
    


        


s = Solution()
print(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates(nums = [0]))
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([]))