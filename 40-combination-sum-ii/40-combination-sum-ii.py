class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total>target or i >= len(candidates):
                return 
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()

#         res = []

#         def backtrack(cur, pos, target):
#             if target == 0:
#                 res.append(cur.copy())
#             if target <= 0:
#                 return

#             prev = -1
#             for i in range(pos, len(candidates)):
#                 if candidates[i] == prev:
#                     continue
#                 cur.append(candidates[i])
#                 backtrack(cur, i + 1, target - candidates[i])
#                 cur.pop()
#                 prev = candidates[i]

#         backtrack([], 0, target)
#         return res