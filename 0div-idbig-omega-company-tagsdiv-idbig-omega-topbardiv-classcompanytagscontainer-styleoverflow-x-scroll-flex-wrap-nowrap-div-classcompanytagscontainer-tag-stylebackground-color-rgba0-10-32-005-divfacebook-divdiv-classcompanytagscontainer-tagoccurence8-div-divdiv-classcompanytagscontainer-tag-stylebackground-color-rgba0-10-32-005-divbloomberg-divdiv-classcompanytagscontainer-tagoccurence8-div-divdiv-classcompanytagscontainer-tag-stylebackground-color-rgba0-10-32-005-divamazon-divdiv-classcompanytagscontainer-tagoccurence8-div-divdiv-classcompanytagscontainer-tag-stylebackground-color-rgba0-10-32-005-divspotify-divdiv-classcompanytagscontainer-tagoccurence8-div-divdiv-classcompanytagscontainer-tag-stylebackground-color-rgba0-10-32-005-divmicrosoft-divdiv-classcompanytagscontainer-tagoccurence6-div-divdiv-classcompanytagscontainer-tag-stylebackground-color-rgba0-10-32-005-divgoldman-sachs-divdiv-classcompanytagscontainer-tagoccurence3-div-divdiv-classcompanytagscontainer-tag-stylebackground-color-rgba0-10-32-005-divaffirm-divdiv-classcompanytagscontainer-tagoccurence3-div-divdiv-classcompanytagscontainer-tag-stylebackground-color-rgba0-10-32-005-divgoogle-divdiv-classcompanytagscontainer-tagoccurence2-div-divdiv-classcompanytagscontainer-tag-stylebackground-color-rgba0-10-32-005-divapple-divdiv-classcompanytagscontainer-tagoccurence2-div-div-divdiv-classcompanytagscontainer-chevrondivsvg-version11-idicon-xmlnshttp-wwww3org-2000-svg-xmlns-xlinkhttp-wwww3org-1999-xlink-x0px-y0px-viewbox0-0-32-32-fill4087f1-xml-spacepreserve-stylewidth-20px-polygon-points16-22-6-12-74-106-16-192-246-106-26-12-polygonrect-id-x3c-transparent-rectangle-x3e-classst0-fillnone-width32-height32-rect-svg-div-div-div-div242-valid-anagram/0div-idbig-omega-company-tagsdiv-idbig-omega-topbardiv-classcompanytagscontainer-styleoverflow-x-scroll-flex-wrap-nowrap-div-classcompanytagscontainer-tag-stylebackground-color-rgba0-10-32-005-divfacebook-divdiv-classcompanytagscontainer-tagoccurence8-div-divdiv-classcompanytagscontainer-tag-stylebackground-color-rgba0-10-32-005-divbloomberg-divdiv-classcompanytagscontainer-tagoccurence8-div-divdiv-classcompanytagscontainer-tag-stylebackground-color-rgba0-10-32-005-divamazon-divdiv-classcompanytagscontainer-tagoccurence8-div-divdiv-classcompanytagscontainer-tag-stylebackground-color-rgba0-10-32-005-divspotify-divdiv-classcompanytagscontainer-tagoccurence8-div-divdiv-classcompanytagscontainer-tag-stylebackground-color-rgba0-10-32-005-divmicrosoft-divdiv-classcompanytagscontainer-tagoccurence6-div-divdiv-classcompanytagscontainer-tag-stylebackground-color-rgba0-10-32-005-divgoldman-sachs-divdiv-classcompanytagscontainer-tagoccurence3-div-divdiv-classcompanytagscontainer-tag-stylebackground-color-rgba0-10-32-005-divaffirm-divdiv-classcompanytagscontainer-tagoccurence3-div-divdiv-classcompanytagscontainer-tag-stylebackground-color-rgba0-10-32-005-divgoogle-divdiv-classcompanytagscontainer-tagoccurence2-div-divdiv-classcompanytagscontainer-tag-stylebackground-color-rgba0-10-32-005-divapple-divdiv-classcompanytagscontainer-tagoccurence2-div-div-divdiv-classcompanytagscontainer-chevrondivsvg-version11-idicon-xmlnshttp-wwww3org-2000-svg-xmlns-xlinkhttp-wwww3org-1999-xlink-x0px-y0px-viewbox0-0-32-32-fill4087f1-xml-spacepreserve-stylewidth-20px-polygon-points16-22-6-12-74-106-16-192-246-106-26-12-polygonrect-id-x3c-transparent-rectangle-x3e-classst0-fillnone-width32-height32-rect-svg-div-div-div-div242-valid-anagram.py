class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = dict()
        for i in s:
            if i in ans.keys():
                ans[i] +=1
            else:
                ans[i] = 1
                
        print(ans)
                
        for i in t:
            if i in ans.keys():
                ans[i] -= 1
            else:
                return False
            
        print(ans)
        print(ans.values())
        for i in ans.values():
            if i != 0:
                return False
        
        return True