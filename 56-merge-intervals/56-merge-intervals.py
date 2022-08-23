class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            prev = res[-1][1]
            cur = intervals[i][0]
            if prev >= cur:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res