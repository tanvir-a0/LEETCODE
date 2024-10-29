class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) >= 3:
            pass
        else:
            return False

        i = 0
        total_increasing = 0
        total_decreasing = 0

        while True:
            if i+1 >= len(arr):
                break
            if arr[i] < arr[i+1]:
                i = i + 1 
                total_increasing = total_increasing + 1
                continue
            else:
                break
            

        while True:
            if i+1 >= len(arr):
                break
            if arr[i] > arr[i+1]:
                i = i + 1 
                total_decreasing = total_decreasing + 1
                continue
            else:
                return False

        print(total_increasing, total_decreasing, total_increasing+total_decreasing)
        if total_increasing == 0 or total_decreasing == 0:
            return False
        
        return True
        
