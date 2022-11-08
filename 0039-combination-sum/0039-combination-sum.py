import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        curr = []
        total = 0
        def backtrack(candidates, i, total):
            if total == target:
                final.append(copy.deepcopy(curr))
                return
            if i == len(candidates) or total>target:
                return 
            # Not select
            backtrack(candidates, i+1, total)
            # Select
            total += candidates[i]
            curr.append(candidates[i])
            backtrack(candidates, i, total)
            total -= candidates[i]
            curr.pop()
        backtrack(candidates, 0, total)
        return final
        