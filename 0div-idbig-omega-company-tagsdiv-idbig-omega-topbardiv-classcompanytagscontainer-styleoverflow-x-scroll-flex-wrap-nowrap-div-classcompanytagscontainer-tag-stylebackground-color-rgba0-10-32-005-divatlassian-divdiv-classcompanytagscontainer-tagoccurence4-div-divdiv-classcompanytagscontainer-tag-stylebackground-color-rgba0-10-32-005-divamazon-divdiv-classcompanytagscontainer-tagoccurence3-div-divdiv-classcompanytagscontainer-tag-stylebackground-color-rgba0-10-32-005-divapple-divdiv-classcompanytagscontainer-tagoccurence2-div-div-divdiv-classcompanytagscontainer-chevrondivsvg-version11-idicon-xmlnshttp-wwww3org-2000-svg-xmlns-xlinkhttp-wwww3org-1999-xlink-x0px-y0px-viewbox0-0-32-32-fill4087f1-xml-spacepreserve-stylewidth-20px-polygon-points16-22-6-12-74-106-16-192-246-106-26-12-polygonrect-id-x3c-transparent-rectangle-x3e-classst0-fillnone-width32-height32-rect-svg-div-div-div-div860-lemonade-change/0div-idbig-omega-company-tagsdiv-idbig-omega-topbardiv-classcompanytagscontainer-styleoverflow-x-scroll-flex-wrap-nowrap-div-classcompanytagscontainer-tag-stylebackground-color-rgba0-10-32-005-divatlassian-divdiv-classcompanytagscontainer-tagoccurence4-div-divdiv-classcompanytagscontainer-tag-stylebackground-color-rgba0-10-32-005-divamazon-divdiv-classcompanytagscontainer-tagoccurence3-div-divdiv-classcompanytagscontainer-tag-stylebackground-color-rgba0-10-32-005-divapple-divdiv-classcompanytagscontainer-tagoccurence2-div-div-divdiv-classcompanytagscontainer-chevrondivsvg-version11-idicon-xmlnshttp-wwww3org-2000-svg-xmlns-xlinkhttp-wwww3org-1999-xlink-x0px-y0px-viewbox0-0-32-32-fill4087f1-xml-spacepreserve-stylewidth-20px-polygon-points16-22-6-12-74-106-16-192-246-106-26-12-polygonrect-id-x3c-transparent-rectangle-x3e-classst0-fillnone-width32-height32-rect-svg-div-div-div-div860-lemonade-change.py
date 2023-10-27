class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {10:0, 5:0}
        i = 0
        while i<len(bills):
            if bills[i]==5:
                d[5]+=1
            elif bills[i]==10:
                d[10]+=1
                if d[5]>=1:
                    d[5]-=1
                else:
                    return False
            elif bills[i]==20:
                if d[10]>=1 and d[5]>=1:
                    d[10]-=1
                    d[5]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
            i+=1
        return True
        