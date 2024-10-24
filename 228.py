class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        temp_li = {}
        index = 0
        for i in range(len(nums)-1):
            #print(nums[i], nums[i+1] + 1)
            if nums[i] + 1 == nums[i + 1] :
                if index not in temp_li:
                    temp_li[index] = []
                temp_li[index].append(nums[i])
            
            else:
                if index not in temp_li:
                    temp_li[index] = []
                temp_li[index].append(nums[i])
                index = index + 1

        if index not in temp_li:
            temp_li[index] = []
        temp_li[index].append(nums[len(nums) - 1])

        ans = []
        for key, value in temp_li.items():
            if len(value) == 1:
                ans.append(str(value[0]))
            else:
                ans.append(str(value[0]) + "->"+ str(value[len(value)-1]))
        
        print(temp_li)
        return ans
        