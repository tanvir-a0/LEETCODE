class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_dic = [0]*k

        for x in arr:
            rem_dic[x%k] = rem_dic[x%k] + 1
        print(rem_dic)

        if rem_dic[0] % 2 != 0:
            return true
        
        for i in range(1, k//2 + 1):
            if rem_dic[i] == rem_dic[k-i]:
                continue
            else:
                return False

        return True
        
