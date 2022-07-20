class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i >=len(candidates):
                return 
            
            # first branch-including the number
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i]) # We keep because we can include more
            # of that numbers in our combinations.
            
            # Second branch-not including the number
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        
        return res
        