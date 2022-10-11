class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
# run the below code in VSCode for detailed explanation
# import collections
# ans = collections.defaultdict(list)
# a = ["tea", "eat", "tan"]
# for i in a:
#     count = [0] * 26
#     print(count)
#     for j in i:
#         count[ord(j) - ord("a")] += 1
#         print(count)
#     ans[tuple(count)].append(i)
#     print(ans)
# print(ans.values())