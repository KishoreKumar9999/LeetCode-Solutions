class Solution:
    def checkValidString(self, s: str) -> bool:
        d = [[0,0]] * len(s)  # d[i][0] represents min_open and d[i][1] represents max_open
        
        min_open, max_open = 0, 0
        
        for i in range(len(s)):
            if s[i] == '(':
                min_open += 1
                max_open += 1
            elif s[i] == '*':
                min_open -= 1  # because * can be )
                max_open += 1  # because * can be (
            else:  # s[i] == ')'
                min_open -= 1
                max_open -= 1
                
            if max_open < 0:  # we have more ) than potential (
                return False
            if min_open < 0:  # reset to zero because we can't have negative open parentheses
                min_open = 0
            
            d[i][0] = min_open
            d[i][1] = max_open
        
        # if we have 0 min_open by the end, it means all can be matched
        return d[-1][0] == 0
