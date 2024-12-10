class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []

        min_abs_diff = max(arr) - min(arr)
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < min_abs_diff:
                min_abs_diff = arr[i+1]-arr[i]

        for i in range(len(arr)-1):
            if arr[i] + min_abs_diff == arr[i+1]:
                res.append( [arr[i], arr[i+1]] )

        #print(res)
        return res


        
