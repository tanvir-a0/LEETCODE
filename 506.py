class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst=sorted(score,reverse=True)
        n=len(lst)
        ans={}
        for i in range(n):
            if i==0:
                ans[lst[i]]="Gold Medal"
            elif i==1:
                ans[lst[i]]="Silver Medal"
            elif i==2:
                ans[lst[i]]="Bronze Medal"
            else:
                ans[lst[i]]=str(i+1)
        res=[]
        for i in score:
            res.append(ans[i])
        return res       
