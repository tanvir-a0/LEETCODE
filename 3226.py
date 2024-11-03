class Solution:
    def minChanges(self, n: int, k: int) -> int:
        a = format(n, '032b')
        b = format(k, '032b')
        print(f"{a}\n{b}")

        a_n = ""
        b_n = ""

        changes = 0
        for i in range(len(a)):
            if a[i] == '1' and b[i] == '0':
                changes = changes + 1
                a_n = a_n + '0'
                b_n = b_n + '0'
                continue
            else:
                a_n = a_n + a[i]
                b_n = b_n + b[i]

        print('changes: ', changes)

        if int(a_n,2) == int(b_n,2):
            return changes
        return -1 
        
